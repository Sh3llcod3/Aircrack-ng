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
        self.setup_parser()

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
        """
        self.parser.add_arg(
            "-b",
            "--bssid",
            "bssid",
            "For certain attacks, specify the AP BSSID",
            optional=False
        )
        self.parser.add_arg(
            "-c",
            "--client-bssid",
            "bssid",
            "For certain attacks, specify the client BSSID",
            optional=False
        )
        self.parser.add_arg(
            "-d",
            "--deauth-count",
            "number",
            "With certain attacks, specify the number of times to send deauth packets",
            optional=False
        )
        self.parser.add_arg(
            "-f",
            "--file",
            "path",
            "For certain operations specify a file path",
            optional=False
        )
        self.parser.add_arg(
            "-w",
            "--wordlist",
            "path",
            "Load the wordlist from the path supplied",
            optional=False
        )
        self.parser.add_arg(
            "-t",
            "--time",
            "seconds",
            "Specify a time value for certain operations, such as scanning for APs",
            optional=False
        )
        """
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
        self.parser.add_comment("If no options are supplied, launch the menu by default.")
        self.parser.parse_args()

        # Manage depedencies

        if self.parser.is_present("-p"):
            path = modules.BASE_PATH
            if path.exists():
                rmtree(path)
                path.mkdir()

        if self.parser.is_present("-i"):
            packages = modules.PackageInstaller()
            packages.install(True)

        if self.parser.is_present("-l"):
            print(modules.CONFIG.read_text())

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

    def show_menu(self) -> None:

        if not len(argv) == 1:
            return

        self.menu_items = [[self.std_aircrack, "Capture handshake and run dictionary attack with aircrack-ng"],
                           [self.pmkid_std, "Capture handshake using PMKID technique and run dictionary attack"],
                           [self.reaver_wps, "Run a Pixiedust attack on select WPS enabled APs with Reaver"],
                           [self.mitm_ap, "Host an MITM AP to phish credentials, sniff traffic and more"],
                           [self.beacon_flood, "Create a beacon flood and fill the air with non-existent AP SSIDs"],
                           [self.crack_cap, "Attempt PSK retrieval with an existing handshake capture file"],
                           [self.manual_control, "Manipulate the system's WiFi cards with full manual control"],
                           [self.install_deps, "(Re)Install the dependencies required for this script"],
                           [self.install_hashcat, "Download and setup Hashcat and Hashcat utils to utilise GPU"]]

        inp = modules.InputManager
        inp.section_type = "main_menu"
        colours = modules.StandardColours()

        while True:
            try:
                cmd = modules.Commands(); cmd.clear()
                colours.deep_red.print_colour(f"Welcome to Airscript-ng {modules.VERSION_STRING} (MIT license)\n")
                for i in enumerate(self.menu_items, start=1):
                    print(f"  {i[0]} - {i[1][-1]}")
                colours.highlight.print_colour("\n99 - Exit")
                print()
                selected = inp("select_option").get(len(self.menu_items), extra=[99])

                if selected == 99 or selected is None:
                    break

                else:
                    self.menu_items[selected - 1][0]()

            except(KeyboardInterrupt, EOFError):
                break

    def std_aircrack(self) -> None:

        packages = modules.PackageInstaller()
        packages.install(False)
        stop_nmgr = False if (self.parser.is_present("-n") or not self.config["stop_nm"]) else True
        aircrack_instance = modules.aircrack(stop_nmgr=stop_nmgr)
        ret = aircrack_instance.scan_aps()
        if ret in [None, False]:
            aircrack_instance.cleanup()
            return
        aircrack_instance.select_target()
        aircrack_instance.deauth_capture()
        aircrack_instance.recover_psk()
        aircrack_instance.cleanup()
        return

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

    def crack_cap(self) -> None:
        ...

    def install_deps(self) -> None:
        ...

    def install_hashcat(self) -> None:
        ...

def main() -> None:

    entrypoint = Airscript()
    entrypoint.load_help()
    entrypoint.show_menu()


if __name__ == "__main__":
    main()
