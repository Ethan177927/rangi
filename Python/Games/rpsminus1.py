"""Rock Paper Scissors Minus One Game."""

import random
import tkinter as tk
from tkinter import *
import subprocess


player_choice = []
button_choice = []
options = ["rock", "paper", "scissors"]
computer_option = []
fcomputerchoice = 1
rpsstreak = 0
highstreak = 0


def rps_game():
    """Start Rock Paper Scissors Game."""
    global rpsstreak, framerps, highstreak
    global username

    try:
        with open("usernames.txt", "r") as f:
            lines = f.readlines()
            username = lines[-1].strip()
    except FileNotFoundError:
        username = "Player"
    print(username)

    # Fonts
    titlefont = ("Helvetica Neue", 30, "bold")
    textfont = ("Helvetica Neue", 15)
    Btnfont = ("Helvetica", 12, "bold")

    rps1 = tk.Tk()

    screen_width = rps1.winfo_screenwidth()
    screen_height = rps1.winfo_screenheight()

    # found off of google to get the screenheigth and width of the user's
    # screen.
    swidth = int(screen_width / 2 - 850 / 2)
    sheight = int(screen_height / 2 - 650 / 2)

    # sets size of the window and the +swidth and +sheight are x,y values for
    # where the window opens on the screen.
    rps1.geometry(f"850x650+{swidth}+{sheight}")
    rps1.configure(bg="#f8f8f8")
    rps1.title("Rock Paper Scissors Minus")
    framerps = Frame(rps1, bg="#f8f8f8")
    streaks = Frame(rps1, bg="#f8f8f8")

    title = Label(
        rps1,
        text="Rock Paper Scissors Minus One",
        font=titlefont,
        bg="#f8f8f8")
    title.pack(padx=10, pady=40)
    welcometext = Label(
        rps1,
        text=f"Welcome {username} to Rock Paper Scissors!",
        font=textfont,
        bg="#f8f8f8")
    welcometext.pack(padx=10, pady=10)

    def BackMenus():
        """Send back to menu."""
        rps1.destroy()
        subprocess.run(["python", r"Python\Games\menu2.py"])
    streaks.pack(pady=5)

    BackMenu = Button(
        rps1,
        text="Back To Menu",
        bg="#f8f8f8",
        font=Btnfont,
        command=BackMenus)
    BackMenu.pack(padx=10, pady=10, side="bottom", anchor='w')
    result = Label(rps1, text="", font=textfont, bg="#f8f8f8")
    result.pack(pady=10)
    streaklabel = Label(
        streaks,
        text=f"Current Win Streak: {rpsstreak}",
        font=textfont,
        bg="#f8f8f8")
    streaklabel.pack(side='left', padx=5)
    highstreaklabel = Label(
        streaks,
        text=f"Highest Win Streak: {highstreak}",
        font=textfont,
        bg="#f8f8f8")
    highstreaklabel.pack(side='left', padx=5)

    def reset_game():
        """Reset the game."""
        player_choice.clear()
        try:
            botselect.destroy()
        except BaseException:
            pass
        try:
            removal.destroy()
        except BaseException:
            pass
        try:
            remove_frame.destroy()
        except BaseException:
            pass
        button_choice.clear()
        computer_option.clear()
        result.config(text="")

        play_btn.pack(padx=10, pady=10)
        framerps.pack_forget()

    def determine(player_final, computer_final):
        """Determine the winner."""
        win_cond = {"rock": "scissors",
                    "scissors": "paper",
                    "paper": "rock"}
        global highstreak
        global rpsstreak
        if player_final == computer_final:
            result.config(text="It's a Tie!")
        elif win_cond[player_final] == computer_final:
            result.config(text="You Win!")
            rpsstreak += 1
            if rpsstreak > highstreak:
                highstreak = rpsstreak
            highstreaklabel.config(text=f"Highest Win Streak: {highstreak}")
        else:
            result.config(text="You Lose!")
            rpsstreak = 0
        streaklabel.config(text=f"Current Win Streak: {rpsstreak}")

        rps1.after(2000, reset_game)

    def check():
        """Display user and bot options."""
        global fcomputerchoice, remove_frame, botselect, removal
        if len(player_choice) == 2:
            for i in range(3):
                if options[i] in player_choice:
                    pass
                else:
                    buttons[i].pack_forget()
            print(
                "You chose: " +
                player_choice[0] +
                " and " +
                player_choice[1])
            print(
                "The computer chose: " +
                computer_option[0] +
                " and " +
                computer_option[1])
            removal = Label(
                rps1,
                text="Remove One!",
                font=textfont,
                bg="#f8f8f8")
            removal.pack(pady=10)
            botselect = Label(
                rps1,
                text=f"The computer is choosing...  {
                    computer_option[0]} or {
                    computer_option[1]}",
                font=textfont,
                bg="#f8f8f8")
            botselect.pack(pady=10)
            framerps.pack_forget()
            remove_frame = Frame(rps1, bg="#f8f8f8")
            remove_frame.pack(pady=10)
            for choice in list(player_choice):
                btn = tk.Button(
                    remove_frame,
                    text=f"Remove {choice.capitalize()}",
                    command=lambda c=choice: player_remove(c),
                    width=20,
                    height=5,
                    font=Btnfont,
                    bg="white",
                    fg="black")
                btn.pack(padx=10, pady=10, side="left")
            fcomputerchoice = random.choice(computer_option)

    def pick(choice, button):
        """Append buttons and choices to list."""
        player_choice.append(choice)
        button_choice.append(button)
        print(choice)
        button.pack_forget()
        check()

    def play():
        """Start Rock Paper Scissors."""
        print("Playing RPS-1")
        welcometext.pack_forget()
        play_btn.pack_forget()
        player_choice.clear()
        button_choice.clear()
        computer_option.clear()

        framerps.pack(pady=20)

        for button in buttons:
            button.pack(padx=10, pady=10, side="left")

        computer_option.append(random.choice(options))
        computer_option.append(random.choice(options))
        if computer_option[0] == computer_option[1]:
            while computer_option[0] == computer_option[1]:
                computer_option[1] = random.choice(options)

    def player_remove(choice):
        """Make user remove choice."""
        for btn in button_choice:
            btn.pack_forget()
        player_choice.remove(choice)
        final_player = player_choice[0]
        determine(final_player, fcomputerchoice)

    play_btn = tk.Button(
        rps1,
        text='Play',
        command=play,
        width=25,
        height=10,
        font=Btnfont,
        bg="white",
        fg="black")
    play_btn.pack(padx=10, pady=10)
    rockbtn = tk.Button(
        framerps,
        text='Rock',
        command=lambda: pick(
            "rock",
            rockbtn),
        width=15,
        height=5,
        font=Btnfont,
        bg="white",
        fg="black")
    paperbtn = tk.Button(
        framerps,
        text='Paper',
        command=lambda: pick(
            "paper",
            paperbtn),
        width=15,
        height=5,
        font=Btnfont,
        bg="white",
        fg="black")
    scissorbtn = tk.Button(
        framerps,
        text='Scissors',
        command=lambda: pick(
            "scissors",
            scissorbtn),
        width=15,
        height=5,
        font=Btnfont,
        bg="white",
        fg="black")

    buttons = [rockbtn, paperbtn, scissorbtn]

    rps1.mainloop()
