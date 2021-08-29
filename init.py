import tkinter as tk
import random
from rockPaperScissors import rockCalculator

rockCalculatorInstance = rockCalculator()

window = tk.Tk()

items = ["rock", "paper", "scissors"]

outcomeText = tk.StringVar()
outcomeText.set("No game has not started yet.")

for item in items:
    tk.Button(
        window,
        text=item,
        command=rockCalculatorInstance.getFightFunc(item, outcomeText)
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
