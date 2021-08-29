import tkinter as tk
import random

items = ["rock", "paper", "scissors"]

class rockCalculator:
    _playerChosenItems = []

    def randomItemChoice(self):
        return items[random.randint(0,2)]

    def getFightFunc(self, item, outcomeText):
        return (lambda : self.fightAndSetOutcomeTest(item, outcomeText))

    def checkLastThreePlayerChoicesAreRock(self):
        result = False
        if(len(self._playerChosenItems) < 4):
            return result

        numberOfRocks = 0
        for i in range(-2,-5,-1):
            if(self._playerChosenItems[i] == "rock"):
                numberOfRocks += 1
        if(numberOfRocks == 3):
            result = True
        return result

    def fight(self, item):
        playerItem = item
        self._playerChosenItems.append(playerItem)
        if(self.checkLastThreePlayerChoicesAreRock()):
            aiItem = "paper"
        else:
            aiItem = self.randomItemChoice()

        outcome = self.determineWinner(playerItem, aiItem)
        return [playerItem, aiItem, outcome]

    def fightAndSetOutcomeTest(self, item, outcomeText):
        outcomeArray = self.fight(item)
        playerItem = outcomeArray[0]
        aiItem = outcomeArray[1]
        outcome = outcomeArray[2]
        outcomeText.set("You chose " + playerItem + " and the ai chose " + aiItem + ". " + outcome)

    def determineWinner(self, playerItem, aiItem):
        if((playerItem == "rock" and aiItem == "scissors") or (playerItem == "paper" and aiItem == "rock") or (playerItem == "scissors" and aiItem == "paper")):
            return "You win!"
        elif((playerItem == "rock" and aiItem == "paper") or (playerItem == "paper" and aiItem == "scissors") or (playerItem == "scissors" and aiItem == "rock")):
            return "You lose!"
        else:
            return "It's a draw!"

