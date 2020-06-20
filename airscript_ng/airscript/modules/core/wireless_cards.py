#!/usr/bin/env python3
from typing import Dict, List

from .constants import ADAPTER_MODES, AIRMON_PATH, IFACES
from .shell_commands import Commands


class card_manager(Commands):

    card_count: int = 0
    total_cards: Dict[int, List[str]] = {}
    selected_cards: Dict[int, List[str]] = {}

    class CardAlreadySelectedError(Exception):
        ...

    class NotAValidCard(Exception):
        ...

    def __init__(self) -> None:

        super().__init__()
        self.card_name: str = ""
        self.card_status: str = ""
        self.card_state: str = ""
        self.chip_set: str = ""
        self.card_driver: str = ""
        self.card_chosen = False

    def load_cards(self, wireless_only: bool = True) -> None:
        card_names = self.capture(f"ls {IFACES} | grep {'^wl' if wireless_only else '-v lo'}").split()

        for i in enumerate(card_names, start=1):

            card_manager.card_count += 1
            BASE = f"{AIRMON_PATH} | grep {i[1]}"
            card_manager.total_cards[i[0]] = [i[1], *self.capture(f"{BASE} | cut -f4", f"{BASE} | cut -f5")]

    def __update_state(self) -> None:
        self.card_status, self.card_state = self.capture(f"iw {self.card_name} info 2>/dev/null "
                                                         "| grep -i type | cut -d ' ' -f 2",
                                                         f"cat /sys/class/net/{self.card_name}/operstate")

    def select_card(self, card_number) -> bool:
        try:
            already_chosen: bool = card_number in card_manager.selected_cards
            valid_card: bool = card_number in card_manager.total_cards

            if already_chosen or self.card_chosen:
                raise self.CardAlreadySelectedError

            elif valid_card:
                current_card = card_manager.total_cards[card_number]
                card_manager.selected_cards[card_number] = current_card
                self.card_name = current_card[0]
                self.__update_state()
                self.card_driver = current_card[1]
                self.chip_set = current_card[2]
                self.card_chosen = True
                del card_manager.total_cards[card_number]
                return True

            else:
                raise self.NotAValidCard

        except(self.CardAlreadySelectedError, self.NotAValidCard):
            return False

    def set_mode(self, mode_type) -> bool:
        try:
            self.run(ADAPTER_MODES[mode_type].format(self.card_name))
            return True

        except(Exception):
            return False
