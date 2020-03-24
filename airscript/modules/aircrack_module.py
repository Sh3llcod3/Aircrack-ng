#!/usr/bin/env python3
import csv
from pathlib import Path as FPath
from secrets import token_hex

from airscript.modules.core import (constants, install_packages,
                                    term_colours, tk_elements, wireless_cards)

from prettytable import PrettyTable


class aircrack(install_packages.PackageInstaller, wireless_cards.card_manager,
               term_colours.StandardColours, tk_elements.TkManager):

    def __init__(self, reset_colours=False, stop_nmgr=True) -> None:
        super().__init__()

        # Check if handshake directory exists.
        if not (constants.HANDSHAKE_FILES.exists() and constants.TEMP_FILES.exists()):
            constants.HANDSHAKE_FILES.mkdir(exist_ok=True)
            constants.TEMP_FILES.mkdir(exist_ok=True)

        term_colours.Colours.reset_colours = reset_colours
        self.InputManager = tk_elements.InputManager
        self.stop_nmgr = stop_nmgr

    def scan_aps(self) -> None:
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
        print(self.card_name)
        print("\n")
        self.green.print_success("Now, let's scan for Access Points.")
        self.green.print_success("Once you see the target AP, press Ctrl-C once.")
        self.blue.print_status("i", "Proceed? y/n\n")
        exp_cfm = self.InputManager("modules/aircrack/explore_aps").get(boolean=True)

        if exp_cfm is None:
            ...

        elif not exp_cfm:
            ...

        self.fpath = constants.TEMP_FILES / token_hex()
        cmd = (f"{constants.AIRODUMP_PATH} -a -w {self.fpath}"
               f" --output-format csv -I 2 -t WPA -t WPA2 -t WPA1 --ignore-negative-one {self.card_name}")
        self.set_mode(1)

        try:
            self.run(cmd)
        except(KeyboardInterrupt, EOFError):
            ...

    def select_target(self) -> None:
        self.clear()
        ap_table = PrettyTable()
        ap_table.field_names = list(self.red.return_colour("No.", "BSSID", "Channel", "Privacy",
                                                           "Cipher", "Auth", "PWR", "ESSID"))
        ap_map = {}
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
                    y_dot = self.yellow.return_colour("*")
                    this_ap = ap_map.get(i[-2].strip())

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
        self.target_ap = num_map.get(self.InputManager("modules/aircrack/select_ap").get(ap_counter))

        if self.target_ap is None:
            ...

    def deauth_capture(self) -> None:
        self.clear()
        opt_table = PrettyTable()
        chosen = 0
        options = [
            "Send Deauth to broadcast & capture handshake",
            "Send Deauth to specific client & capture handshake",
            "Don't send Deauths, listen passively for handshake"
        ]
        opt_table.field_names = [self.green.return_colour("No."), self.yellow.return_colour("Action")]
        for i in enumerate(options, start=1):
            opt_table.add_row(i[0], i[1])

        print(opt_table, end="\n\n")
        self.blue.print_status("i", "Please enter integer relating to desired action.\n")
        chosen = self.InputManager("modules/aircrack/deauth_selection").get(i[0])

        if chosen is None:
            ...

        elif chosen == 1:
            ...

        elif chosen == 2:
            ...

        elif chosen == 3:
            ...

    def recover_psk(self) -> None:
        ...

    def cleanup(self) -> None:
        self.set_mode(0)
        self.nm_start()
