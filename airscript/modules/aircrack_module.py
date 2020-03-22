#!/usr/bin/env python3

from airscript.modules.core import (constants, install_packages,
                                    term_colours, tk_elements, wireless_cards)

from prettytable import PrettyTable


class aircrack(install_packages.PackageInstaller, wireless_cards.card_manager,
               term_colours.StandardColours, tk_elements.TkManager):

    def __init__(self, reset_colours=False) -> None:
        super().__init__()

        # Check if handshake directory exists.
        if not constants.HANDSHAKE_FILES.exists():
            constants.HANDSHAKE_FILES.mkdir()

        term_colours.Colours.reset_colours = reset_colours
        self.InputManager = tk_elements.InputManager

    def scan_aps(self) -> None:
        self.clear()
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
        self.green.print_success("Now, let's scan for Access Points.")
        self.green.print_success("Once you see the target AP, press Ctrl-C once.")
        self.blue.print_status("i", "Proceed? y/n\n")
        exp_cfm = self.InputManager("modules/aircrack/explore_aps").get(boolean=True)

        if exp_cfm:
            self.set_mode(1)

        elif exp_cfm is None:
            ...

        else:
            ...

    def select_target(self) -> None:
        ...

    def deauth_capture(self) -> None:
        ...

    def recover_psk(self) -> None:
        ...

    def cleanup(self) -> None:
        ...
