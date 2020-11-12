#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
from shutil import rmtree
from sys import argv, exit

from airscript_ng.airscript import modules

import easyparse

# 8 discrete types of attacks on wifi + mdk fun + DOS


class Airscript():

    def __init__(self) -> None:
        self.cfparser = configparser.ConfigParser()
        self.cfparser.read(modules.CONFIG)
        self.config = {}
        self.colours = modules.StandardColours()
        self.setup_parser()
        self.inp = modules.InputManager("main_menu", "options")

        for i in self.cfparser["airscript"].items():
            self.config[i[0]] = True if i[1] == "yes" else False

    def setup_parser(self) -> None:

        # Setup argument parser
        self.parser: easyparse.opt_parser = easyparse.opt_parser(argv)
        self.parser.add_arg(
            "-h",
            "--help",
            None,
            "Show help screen and exit.",
            optional=True
        )
        self.parser.add_arg(
            "-v",
            "--version",
            None,
            "Show version info and exit.",
            optional=True
        )
        self.parser.add_arg(
            "-m",
            "--mode",
            "option",
            "Skip menu, run directly specified menu option",
            optional=False
        )
        self.parser.add_arg(
            "-n",
            "--no-stop-nm",
            None,
            "Don't stop the network-manager when using over SSH (unstable)",
            optional=False
        )
        self.parser.add_arg(
            "-i",
            "--install-deps",
            None,
            "Compile and install the required dependencies",
            optional=False
        )
        self.parser.add_arg(
            "-r",
            "--read-config",
            "file",
            "Read the config file specified instead of the default",
            optional=False
        )
        self.parser.add_arg(
            "-p",
            "--purge",
            None,
            "Delete the directory containing dependencies",
            optional=False
        )
        self.parser.add_arg(
            "-e",
            "--edit-config",
            "key=value",
            "Change a value in the default config file (e.g -e stop_nm=yes)",
            optional=True
        )
        self.parser.add_arg(
            "-l",
            "--list-config",
            None,
            "Print the current configuration settings for airscript-ng",
            optional=True
        )
        self.parser.add_arg(
            "-s",
            "--skip-colors",
            None,
            "Don't show colorised terminal output for terminals which don't support ANSI colors",
            # https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
            optional=True
        )
        self.parser.parse_args()

    def load_help(self) -> None:

        # Show help screen
        if self.parser.is_present("-s") or not self.config["enable_color"]:
            self.parser._opt_parser__add_blank_colors()
            modules.Colours.reset_colours = True

        if self.parser.is_present("-h"):
            self.parser.filename = "airscript-ng"
            self.parser.show_help()
            exit(0)

        # Show version information
        elif self.parser.is_present("-v"):
            print(modules.VERSION_STRING)
            exit(0)

    def manage_args(self) -> None:

        # Manage dependencies
        if self.parser.is_present("-p"):
            path = modules.BASE_PATH
            if path.exists():
                rmtree(path)
                path.mkdir()
                self.colours.deep_green.print_success("Removed folder with dependencies")
                exit(0)

        if self.parser.is_present("-i"):
            packages = modules.PackageInstaller()
            packages.install(True)
            exit(0)

        if self.parser.is_present("-l"):
            print(modules.CONFIG.read_text())
            exit(0)

    def show_menu(self) -> None:

        colours = self.colours
        self.menu_items = [[self.std_aircrack, colours.deep_green.return_colour(
                            "Capture handshake and run dictionary attack with aircrack-ng")],
                           [self.pmkid_std, colours.deep_blue.return_colour(
                            "Capture handshake using RSN PMKID and run dictionary attack")],
                           [self.reaver_wps, colours.deep_pink.return_colour(
                            "Run a Pixiedust attack on select WPS enabled APs with Reaver")],
                           [self.deauth_fun, colours.deep_red.return_colour(
                            "Flood a target client or access point with deauth/disassoc packets")],
                           [self.mitm_ap, colours.deep_yellow.return_colour(
                            "Host an MITM AP to phish credentials, sniff traffic and more")],
                           [self.beacon_flood, colours.deep_green.return_colour(
                            "Create a beacon flood and fill the air with non-existent SSIDs")],
                           [self.crack_cap, colours.deep_red.return_colour(
                            "Attempt PSK retrieval with an existing handshake capture file")],
                           [self.manual_control, colours.deep_blue.return_colour(
                            "Manipulate the system's WiFi cards with full manual control")],
                           [self.install_deps, colours.deep_yellow.return_colour(
                            "(Re)Install the dependencies required for this script")],
                           [self.install_hashcat, colours.deep_pink.return_colour(
                            "Download and setup Hashcat and Hashcat utils to utilise GPU")]]

        while True:
            try:
                modules.Commands().clear()
                colours.deep_red.print_colour(f"Welcome to Airscript-ng {modules.VERSION_STRING} (MIT license)\n")
                for i in enumerate(self.menu_items, start=1):
                    print(f"  [{colours.deep_green.return_colour(i[0])}] - {i[1][-1]}")
                print("\n  ", end="")
                colours.highlight.print_colour("[99] - Exit")
                print()
                selected = self.inp.get(len(self.menu_items), extra=[99], pos="choose")

                if selected == 99 or selected is None:
                    break

                else:
                    self.menu_items[selected - 1][0]()
                    if self.inp.exit_prompt():
                        continue
                    else:
                        modules.Commands.quit(0)

            except(KeyboardInterrupt, EOFError):
                break

    def std_aircrack(self) -> None:

        self.inp.section_type = "attacks"
        packages = modules.PackageInstaller()
        packages.install(False)
        aircrack_instance = modules.aircrack(
            stop_nmgr=False if (self.parser.is_present("-n") or not self.config["stop_nm"]) else True
        )

        if aircrack_instance.scan_aps() in [None, False]:
            aircrack_instance.cleanup()
            return

        aircrack_instance.select_target()
        aircrack_instance.deauth_capture()
        aircrack_instance.recover_psk()
        aircrack_instance.cleanup()

    def pmkid_std(self) -> None:
        ...

    def reaver_wps(self) -> None:
        ...

    def mitm_ap(self) -> None:
        ...

    def manual_control(self) -> None:
        ...

    def beacon_flood(self) -> None:
        ...

    def deauth_fun(self) -> None:
        ...

    def crack_cap(self) -> None:
        ...

    def install_deps(self) -> None:
        ...

    def install_hashcat(self) -> None:
        ...


def main() -> None:

    entrypoint = Airscript()
    entrypoint.manage_args()
    entrypoint.load_help()
    entrypoint.show_menu()


if __name__ == "__main__":
    main()
