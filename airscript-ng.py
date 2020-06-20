#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
from shutil import rmtree
from sys import argv, exit

from airscript import modules

import easyparse

# 8 discrete types of attacks on wifi + mdk fun + DOS


def main() -> None:

    cfparser = configparser.ConfigParser()
    cfparser.read('config.cfg')
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
        "Skip menu, run directly specified menu option",
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
        "Compile and install the required dependencies.",
        optional=False
    )
    parser.add_arg(
        "-c",
        "--config",
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
    parser.parse_args()

    # Show help screen
    if parser.is_present("-h") or len(argv) == 1:
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
        from airscript.modules.core.install_packages import PackageInstaller
        packages = PackageInstaller()
        packages.install(True)


if __name__ == "__main__":
    main()
