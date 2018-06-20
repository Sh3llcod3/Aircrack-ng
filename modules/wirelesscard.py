#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   wirelesscard.py - Manage wireless cards for airscript-ng.
#    Copyright (C) 2018 Yudhajit N. (Sh3llcod3)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>
#   Contact: Please create a issue on my GitHub <https://github.com/Sh3llcod3>
#
#Import the needed function
from .run_command import bashRun, ioStream, bashReturnValue
#Define the class to manage the card here
class wirelessCard(object):
    chosenCardCount = 0
    chosenCards = {}
    totalCards = {}
    totalCardChipsets = {}
    totalCardCount = 0
    def __init__(self,cardName=None):
        self.cardName = cardName
        self.status = None
        self.cardChipset = None
    def setMonitorMode(self):
        if self.status != "Monitor" and self.status != "Unmanaged":
            bashRun("ip link set {0} down; iw dev {0} set type monitor; ip link set {0} up".format(self.cardName))
            self.status = "Monitor"
    def setManagedMode(self):
        if self.status != "Managed" and self.status != "Unmanaged":
            bashRun("ip link set {0} down; iw dev {0} set type managed; ip link set {0} up".format(self.cardName))
            self.status = "Managed"
    def setAlternativeMonitorMode(self):
        if self.status != "Monitor" and self.status != "Unmanaged":
            bashRun("ifconfig {0} down; iwconfig {0} mode monitor; ifconfig {0} up".format(self.cardName))
            self.status = "Monitor"
    def setAlternativeManagedMode(self):
        if self.status != "Managed" and self.status != "Unmanaged":
            bashRun("ifconfig {0} down; iwconfig {0} mode managed; ifconfig {0} up".format(self.cardName))
            self.status = "Managed"
    def setStateUnmanaged(self):
        bashRun("nmcli dev set {0} managed no".format(self.cardName))
        self.status = "Unmanaged"
    def setStateManaged(self):
        if self.status == "Unmanaged":
            bashRun("nmcli dev set {0} managed yes".format(self.cardName))
            self.status = "Managed"
    def enumerateCards(self,showAllCards=False):
        if showAllCards:
            cardCommandCounter = "ls /sys/class/net/ | grep -v lo | wc -l"
            cardCommandListCard = "ls /sys/class/net/ | grep -v lo | "
        else:
            cardCommandCounter = "ls /sys/class/net/ | grep ^wl | wc -l"
            cardCommandListCard = "ls /sys/class/net/ | grep ^wl | "
        wirelessCard.totalCardCount = int(ioStream(cardCommandCounter))
        wirelessCard.totalCards.clear()
        wirelessCard.totalCardChipsets.clear()
        for cardIndex in range(1,wirelessCard.totalCardCount + 1):
            wirelessCard.totalCards[cardIndex] = ioStream(cardCommandListCard + "head -n {} | tail -n 1".format(cardIndex))
        for CardNumber in wirelessCard.totalCards.keys():
            currentCardName = wirelessCard.totalCards[CardNumber]
            getChipsetCommand = "~/.airscriptNG/air/*/scripts/airmon-ng "
            getChipsetCommand += "| grep {} | ".format(currentCardName)
            getChipsetCommand += "awk -F ' ' {'print $4,$5,$6,$7,$8,$9,$10'}"
            currentCardChipset = ioStream(getChipsetCommand)
            if currentCardChipset == str():
                currentCardChipset = "Non wifi device"
            wirelessCard.totalCardChipsets[CardNumber] = currentCardChipset
    def listCards(self,colorClass):
        totalCards = wirelessCard.totalCards
        totalCardChipsets = wirelessCard.totalCardChipsets
        for i in zip(totalCards.keys(),totalCards.values()):
            currentCardToPrint = "{}#{}:".format(colorClass.red_deep,colorClass.endl)
            currentCardToPrint += " {}{}{}".format(colorClass.blue_deep,i[0],colorClass.endl)
            currentCardToPrint += " {}Interface{}:".format(colorClass.green_deep,colorClass.endl)
            currentCardToPrint += " {}{}{}".format(colorClass.blue_deep,i[1],colorClass.endl)
            currentCardToPrint += " {}Chipset{}:".format(colorClass.yellow_deep,colorClass.endl)
            currentCardToPrint += " {}{}{}".format(colorClass.blue_deep,totalCardChipsets[i[0]],colorClass.endl)
            print(currentCardToPrint)
    def chooseCard(self,chosenCardNumber):
        try:
            self.cardName = wirelessCard.totalCards[chosenCardNumber]
            self.cardChipset = wirelessCard.totalCardChipsets[chosenCardNumber]
            if self.cardName not in wirelessCard.chosenCards.values():
                wirelessCard.chosenCards[chosenCardNumber] = self.cardName
                wirelessCard.chosenCardCount += 1
                del wirelessCard.totalCards[chosenCardNumber]
                del wirelessCard.totalCardChipsets[chosenCardNumber]
                wirelessCard.totalCardCount -= 1
                return True
            else:
                raise NameError
        except(KeyError,NameError):
            return False
    def verifyChosenCard(self,selectedCardNumber):
        if selectedCardNumber in self.totalCards.keys():
            return True
        else:
            return False
    def resetCards(self,optionShowAllCards=False):
        wirelessCard.chosenCardCount = 0
        wirelessCard.chosenCards.clear()
        self.enumerateCards(optionShowAllCards)