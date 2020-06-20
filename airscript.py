#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
from shutil import rmtree
from sys import argv, exit

from airscript_ng.airscript import modules

import easyparse

# 8 discrete types of attacks on wifi + mdk fun + DOS


def main() -> None:

    cfparser = configparser.ConfigParser()
    cfparser.read(modules.core.constants.CONFIG)
    config = {}
    for i in cfparser["airscript"].items():
        config[i[0]] = True if "yes" else False

    # Setup argument parser
    parser: easyparse.opt_parser = easyparse.opt_parser(argv)
    parser.add_arg(
        "-h",
        "--help",
        None,
        "Show help screen and exit.",
        optional=True
    )
    parser.add_arg(
        "-v",
        "--version",
        None,
        "Show version info and exit.",
        optional=True
    )
    parser.add_arg(
        "-m",
        "--mode",
        "option",
        "Skip menu, run directly specified menu option with supplied arguments",
        optional=False
    )
    parser.add_arg(
        "-n",
        "--no-stop-nm",
        None,
        "Don't stop the network-manager when using over SSH (unstable)",
        optional=False
    )
    parser.add_arg(
        "-i",
        "--install-deps",
        None,
        "Compile and install the required dependencies",
        optional=False
    )
    parser.add_arg(
        "-r",
        "--read-config",
        "file",
        "Read the config file specified instead of the default",
        optional=False
    )
    parser.add_arg(
        "-p",
        "--purge",
        None,
        "Delete the directory containing dependencies",
        optional=False
    )
    parser.add_arg(
        "-b",
        "--bssid",
        "bssid",
        "For certain attacks, specify the AP BSSID",
        optional=False
    )
    parser.add_arg(
        "-c",
        "--client-bssid",
        "bssid",
        "For certain attacks, specify the client BSSID",
        optional=False
    )
    parser.add_arg(
        "-d",
        "--deauth-count",
        "number",
        "With certain attacks, specify the number of times to send deauth packets",
        optional=False
    )
    parser.add_arg(
        "-f",
        "--file",
        "path",
        "For certain operations specify a file path",
        optional=False
    )
    parser.add_arg(
        "-w",
        "--wordlist",
        "path",
        "Load the wordlist from the path supplied",
        optional=False
    )
    parser.add_arg(
        "-t",
        "--time",
        "seconds",
        "Specify a time value for certain operations, such as scanning for APs",
        optional=False
    )
    parser.add_arg(
        "-e",
        "--edit-config",
        "key=value",
        "Change a value in the default config file (e.g -e stop_nm=yes,enable_color=no)",
        optional=True
    )
    parser.add_arg(
        "-l",
        "--list-config",
        None,
        "Print the current configuration settings for airscript-ng",
        optional=True
    )
    parser.add_arg(
        "-s",
        "--show-no-colors",
        None,
        "Don't show colorised terminal output for terminals which don't support ANSI colors",
        # https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
        optional=False
    )
    parser.add_comment("If no options are supplied, launch the menu by default.")
    parser.parse_args()

    # Show help screen
    if parser.is_present("-s"):
        parser._opt_parser__add_blank_colors()
        modules.core.term_colours.Colours.reset_colours = True

    if parser.is_present("-h"):
        parser.filename = "airscript-ng"
        parser.show_help()
        exit(0)

    # Show version information
    elif parser.is_present("-v"):
        print(modules.core.VERSION_STRING)
        exit(0)

    # Manage depedencies

    if parser.is_present("-p"):
        path = modules.core.constants.BASE_PATH
        if path.exists():
            rmtree(path)
            path.mkdir()

    if parser.is_present("-i"):
        from modules.core.install_packages import PackageInstaller
        packages = PackageInstaller()
        packages.install(True)

    if parser.is_present("-l"):
        print(modules.core.constants.CONFIG.read_text())


if __name__ == "__main__":
    main()
