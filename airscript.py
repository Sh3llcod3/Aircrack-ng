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
        self.cfparser.read(modules.core.constants.CONFIG)
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
            "Skip menu, run directly specified menu option with supplied arguments",
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
            path = modules.core.constants.BASE_PATH
            if path.exists():
                rmtree(path)
                path.mkdir()

        if self.parser.is_present("-i"):
            from modules.core.install_packages import PackageInstaller
            packages = PackageInstaller()
            packages.install(True)

        if self.parser.is_present("-l"):
            print(modules.core.constants.CONFIG.read_text())

    def load_help(self) -> None:

        # Show help screen
        if self.parser.is_present("-s") or not self.config["enable_color"]:
            self.parser._opt_parser__add_blank_colors()
            modules.core.term_colours.Colours.reset_colours = True

        if self.parser.is_present("-h"):
            self.parser.filename = "airscript-ng"
            self.parser.show_help()
            exit(0)

        # Show version information
        elif self.parser.is_present("-v"):
            print(modules.core.VERSION_STRING)
            exit(0)

    def show_menu(self) -> None:

        self.menu_items = [self.std_aircrack,
                           self.reaver_wps,
                           self.mitm_ap,
                           self.beacon_flood,
                           self.crack_cap,
                           self.install_deps,
                           self.install_hashcat]

    def std_aircrack(self) -> None:
        ...

    def reaver_wps(self) -> None:
        ...

    def mitm_ap(self) -> None:
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


if __name__ == "__main__":
    main()
