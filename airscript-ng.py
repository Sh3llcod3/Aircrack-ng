#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv, exit

from airscript import modules

import easyparse


def main() -> None:

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
    parser.parse_args()

    # Show help screen
    if parser.is_present("-h"):
        parser.filename = "airscript-ng"
        parser.show_help()
        exit(0)

    # Show version information
    elif parser.is_present("-v"):
        print(modules.core.VERSION_STRING)
        exit(0)


if __name__ == "__main__":
    main()
