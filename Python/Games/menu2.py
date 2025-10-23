"""Main Menu without the name entry."""


import tkinter as tk
from tkinter import *

# Fonts
titlefont = ("Helvetica Neue", 30, "bold")
textfont = ("Helvetica Neue", 15)
btnfont = ("Helvetica", 12, "bold")
gamefont = ("Helvetica", 15, "bold")

def tk_window():
    """Create Tk window."""
    global username

    try:
        with open("usernames.txt", "r") as f:
            lines = f.readlines()
            username = lines[-1].strip()
    except FileNotFoundError:
        username = "Player"
    print(username)

    tkmain = tk.Tk()

    tkmain.title("Alston Games Comependium")

    screen_width = tkmain.winfo_screenwidth()
    screen_height = tkmain.winfo_screenheight()

    # found off of google to get the screenheigth and width of the user's
    # screen.
    swidth = int(screen_width / 2 - 850 / 2)
    sheight = int(screen_height / 2 - 650 / 2)

    # sets size of the window and the +swidth and +sheight are x,y values for
    # where the window opens on the screen.
    tkmain.geometry(f"850x650+{swidth}+{sheight}")
    tkmain.configure(bg='#f8f8f8')

    # creates the title of the game.
    title = Label(
        tkmain,
        text="Alston Games Compendium",
        font=titlefont,
        bg="#f8f8f8")
    title.pack(padx=10, pady=40)
    welcometext = Label(
        tkmain,
        text=f"What game would you like to play next {username}?",
        font=textfont,
        bg="#f8f8f8")
    welcometext.pack(padx=10, pady=10)

    def minesweepers():
        """Open Minesweeper."""
        print("Minesweeper opening...")
        tkmain.destroy()
        import minesweeper
        minesweeper.minesweeper_game()

    def rpsgame():
        """Open Rock Paper Scissors."""
        print("Rock Paper Scissors opening...")
        tkmain.destroy()
        import rpsminus1
        rpsminus1.rps_game()

    def vmt():
        """Open Visual Memory Test."""
        print("visual Memory Test opening...")
        tkmain.destroy()
        import visualmemorytest
        visualmemorytest.vmt()
    row_frame = Frame(tkmain, bg='#f8f8f8')
    row_frame.pack(pady=10)

    minesweep = tk.Button(
        row_frame,
        text="Minesweeper",
        font=gamefont,
        bg="#f8f8f8",
        fg="black",
        width=20,
        height=4,
        command=minesweepers)
    minesweep.grid(row=0, column=0, padx=10, pady = 10)
    rps = tk.Button(
        row_frame,
        text="Rock Paper Scissors",
        font=gamefont,
        bg="#f8f8f8",
        fg="black",
        width=20,
        height=4,
        command=rpsgame)
    rps.grid(row=1, column=0, padx=10, pady = 10)
    vmt = tk.Button(
        row_frame,
        text="Visual Memory Test",
        font=gamefont,
        bg="#f8f8f8",
        fg="black",
        width=20,
        height=4,
        command=vmt)
    vmt.grid(row=2, column=0, padx=10, pady = 10)
    leaderboard = Label(
        tkmain,
        text="Leaderboard",
        font=textfont,
        bg="#f8f8f8")

    tkmain.mainloop()


tk_window()
