import tkinter as tk
import random

window = tk.Tk()

items = ["rock", "paper", "scissors"]

outcomeText = tk.StringVar()
outcomeText.set("No game has not started yet.")

def aiChoosesRandomItem():
    return items[random.randint(0,2)]

def getFightFunc(item):
    return (lambda : fight(item))

def fight(item):
    playerItem = item
    aiItem = aiChoosesRandomItem()
    outcome = determineWinner(playerItem, aiItem)
    outcomeText.set("You chose " + playerItem + " and the ai chose " + aiItem + ". " + outcome)


def determineWinner(playerItem, aiItem):
    if((playerItem == "rock" and aiItem == "scissors") or (playerItem == "paper" and aiItem == "rock") or (playerItem == "scissors" and aiItem == "paper")):
        return "You win!"
    elif((playerItem == "rock" and aiItem == "paper") or (playerItem == "paper" and aiItem == "scissors") or (playerItem == "scissors" and aiItem == "rock")):
        return "You lose!"
    else:
        return "It's a draw!"



for item in items:
    tk.Button(
        window,
        text=item,
        command=getFightFunc(item)
    ).pack()

outcomeFrame = tk.Frame(
    window,
    width = 400,
    height= 50
    )
outcomeFrame.pack()

tk.Label(
    outcomeFrame,
    textvariable=outcomeText
).place(
    y=0,
    width=400,
    height=50
)




window.mainloop()





