from tkinter import *
from tkinter import messagebox
import random

start = Tk()
start.title('Rock, Paper, Scissors')
start.geometry('400x200')

label1 = Label(start,
               text = 'Hey User! Welcome to Rock, Paper, Scissors.',
               fg = 'black',
               font = ('Arial', 13))
label1.pack(pady=20, padx=20)

def msg():
    MsgBox = messagebox.showinfo(
        'Start', 'Do you want to play the game?', icon = 'question', type = 'yesno')
    if MsgBox == 'yes':
        initiate()

button1 = Button(start,
                 text = "Let's get started",
                 command = msg,
                 bg='brown',
                 fg='white')
button1.pack(pady=10)

def initiate():
    game = Toplevel()
    game.title("Rock, Paper, Scissors")
    game.geometry('600x600')

    label = Label(game, text="Enter your weapon", font=('Arial', 12))
    entry = Entry(game)
    lbl = Label(game, text="Here are the results", font=('Arial', 12))

    playerlabel = Label(game, text="Player's Choice:", font=('Arial', 10))
    botlabel = Label(game, text="Computer's Choice:", font=('Arial', 10))

    player = Entry(game, text="rock/paper/scissors")
    bot = Entry(game)
    res = Entry(game)
    options = ["rock", "paper", "scissors"]

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

    def result():
        user = entry.get().strip().lower()
        if user not in options:
            messagebox.showerror("Invalid input", "Please enter rock, paper or scissors.")
            return
        computer = random.choice(options)

        player.delete(0, END)
        bot.delete(0, END)
        res.delete(0, END)

        player.insert(0, user)
        bot.insert(0, computer)
        outcome = determine_winner(user, computer)
        res.insert(0, outcome)

    btn = Button(game, text="enter", command=result, bg='brown', fg='white')

    label.pack(pady=20)
    entry.pack(pady=10)
    btn.pack(pady=10)
    lbl.pack(pady=20)

    playerlabel.place(x=150, y=250)
    botlabel.place(x=150, y=300)

    player.place(x=350, y=250)
    bot.place(x=350, y=300)
    res.place(x=250, y=400)

    game.mainloop()

start.mainloop()