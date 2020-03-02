#!/usr/bin/env python3
from typing import Dict, List

from .constants import ADAPTER_MODES, AIRMON_PATH, IFACES
from .shell_commands import Commands


class card_manager(Commands):

    card_count: int = 0
    total_cards: Dict[int, List[str]] = {}

    def __init__(self) -> None:

        super().__init__()
        self.card_name: str = ""
        self.card_status: str = ""
        self.chip_set: str = ""

    def load_cards(self, wireless_only: bool = True) -> None:

        for i in enumerate(self.capture(f"ls {IFACES} | grep {'^wl' if wireless_only else '-v lo'}").split("  ")):

            card_manager.card_count += 1
            card_manager.total_cards[i[0]] = [i[1], self.capture(f"{AIRMON_PATH} | grep {i[1]} | cut -f4")]

    def select_card(self) -> bool:
        print(card_manager.total_cards.items())
        return True

    def set_mode(self, mode_type) -> bool:
        self.run(ADAPTER_MODES[mode_type].format(self.card_name))
        return True
