#!/usr/bin/env python3
from typing import Dict

from .shell_commands import Commands


class card_manager(Commands):

    card_count: int = 0
    total_cards: Dict = {}

    def __init__(self) -> None:

        super().__init__()
        self.card_name: str = ""
        self.card_status: str = ""
        self.chip_set: str = ""

    def load_cards(self, wireless_only: bool = True) -> bool:
        ...
