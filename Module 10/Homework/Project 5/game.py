from tkinter import *
import random
from tkinter import messagebox

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (user == "rock" and computer == "scissors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"):
        return "You win!"
    if (user == "rock" and computer == "paper") or \
        (user == "scissors" and computer == "rock") or \
        (user == "paper" and computer == "scissors"):
        return "You lose!"

def play_game(user):
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    result = determine_winner(user, computer)
    messagebox.showinfo("Result", f"You chose {user}. Computer chose {computer}.\n{result}")

def rock():
    play_game("rock")

def paper():
    play_game("paper")

def scissors():
    play_game("scissors")

window = Tk()
window.title("Rock, Paper, Scissors")

label = Label(window, text="Choose your weapon!")
label.pack(pady=10)

rock = Button(window, text="Rock", width=10, command=rock)
rock.pack(pady=5)

paper = Button(window, text="Paper", width=10, command=paper)
paper.pack(pady=5)

scissors = Button(window, text="Scissors", width=10, command=scissors)
scissors.pack(pady=5)

window.mainloop()