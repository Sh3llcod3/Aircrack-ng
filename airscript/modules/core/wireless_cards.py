#!/usr/bin/env python3
from typing import Dict

from .constants import IFACES
from .shell_commands import Commands


class card_manager(Commands):

    card_count: int = 0
    total_cards: Dict = {}

    def __init__(self) -> None:

        super().__init__()
        self.card_name: str = ""
        self.card_status: str = ""
        self.chip_set: str = ""

    def load_cards(self, wireless_only: bool = True) -> None:

        for i in enumerate(self.capture(f"ls {IFACES} | grep {'^wl' if wireless_only else '-v lo'}").split("  ")):

            card_manager.card_count += 1
            card_manager.total_cards[i[0]] = i[1]  # [i[1], self.capture(f"{AIRMON_PATH} | grep {i[1]} | cut -f4")]
