#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Colours():
    '''
    A class to display colours in 256 colour terminals.
    It uses ansi colour codes as objects, with methods
    that can print various status messages, or just
    colourise the output in general. You as the user
    are free to add any colours you want, as long as
    you have the ansi code for it.
    '''
    reset_colours = False

    # Setup our __init__ method.
    def __init__(self, colour_code) -> None:
        self.colour_code: str = colour_code

        # The code that returns colour to normal.
        self.end_code: str = "\033[0m"

    # Add a base method for printing statuses
    def print_status(self, symbol, message) -> None:

        if not Colours.reset_colours:
            print(f"{self.colour_code}[{symbol}]{self.end_code}", message)

        else:
            print(f"[{symbol}]", message)

    # Add method to print a success message.
    def print_success(self, message) -> None:
        self.print_status("+", message)

    # Add method to print a failed message.
    def print_fail(self, message) -> None:
        self.print_status("-", message)

    # Add a method to print a question.
    def print_question(self, message) -> None:
        self.print_status("?", message)

    # Add a method to print an unsure message.
    def print_unsure(self, message) -> None:
        self.print_status("~", message)

    # Add method to simply print the colourised text.
    def print_colour(self, message) -> None:
        if not Colours.reset_colours:
            print(self.colour_code + message + self.end_code)
        else:
            print(message)

    # Add a method to return a status message.
    def return_status(self, symbol, message) -> str:
        if not Colours.reset_colours:
            return f"{self.colour_code}[{symbol}]{self.end_code} {message}"
        else:
            return f"[{symbol}] {message}"

    # Add a method to return the colourised text.
    def return_colour(self, message) -> str:
        if not Colours.reset_colours:
            return f"{self.colour_code}{message}{self.end_code}"
        else:
            return message
