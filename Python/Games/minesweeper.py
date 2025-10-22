"""Minesweeper Game in Python using Tkinter."""

import tkinter as tk
from tkinter import *
import time
import subprocess
timed = []
# py -m autopep8 --in-place --aggressive --aggressive

height = -1
easytime = 0
mediumtime = 0
hardtime = 0


def minesweeper_game():
    """Create the Minesweeper Game."""
    global username

    try:
        with open("usernames.txt", "r") as f:
            lines = f.readlines()
            username = lines[-1].strip()
    except FileNotFoundError:
        username = "Player"
    print(username)

    global flags, mines, width, height, Mine_list, surrounding
    global clicked_tile, ctiles, clicked_x, clicked_y, clicked_first
    tkmine = tk.Tk()
    tkmine.configure(bg="#f8f8f8")
    tkmine.title("Minesweeper Game")
    # Fonts
    titlefont = ("Helvetica Neue", 30, "bold")
    textfont = ("Helvetica Neue", 15)
    btnfont = ("Helvetica", 12, "bold")

    titlemine = Label(
        tkmine,
        text="Minesweeper",
        font=titlefont,
        fg="black",
        bg="#f8f8f8")
    titlemine.pack(padx=10, pady=10)

    screen_width = tkmine.winfo_screenwidth()
    screen_height = tkmine.winfo_screenheight()

    # found off of google to get the screenheigth and width of the user's
    # screen.
    swidth = int(screen_width / 2 - 850 / 2)
    sheight = int(screen_height / 2 - 650 / 2)

    # sets size of the window and the +swidth and +sheight are x,y values for
    # where the window opens on the screen.
    tkmine.geometry(f"850x650+{swidth}+{sheight}")

    Mine_list = []
    surrounding = []
    import random
    global Game_overMS
    Game_overMS = 1
    flags = 0
    flags_label = Label(
        tkmine,
        text=f"Flags remaining: {flags} ",
        font=textfont,
        bg="#f8f8f8")
    flags_label.pack(padx=10, pady=10)

    welcometext = Label(
        tkmine,
        text=f"Welcome {username} to Minesweeper!",
        font=textfont,
        bg="#f8f8f8")
    welcometext.pack(padx=10, pady=10)

    def backmenu():
        """Transport back to menu."""
        tkmine.destroy()
        subprocess.run(["python", r"Python\Games\menu2.py"])

    backmenus = Button(
        tkmine,
        text="Back To Menu",
        bg="#f8f8f8",
        font=btnfont,
        command=backmenu)
    backmenus.pack(padx=10, pady=10, side="bottom", anchor='w')

    global text
    text = Label(
        tkmine,
        text="Left click to reveal a tile,"
        " right click to place/remove a flag.",
        font=textfont,
        bg="#f8f8f8")
    text.pack(padx=10)

    def set_difficulty(level):
        """Set difficulty of game."""
        global Difficulty, grid_size, flags, mines, width, height, midx, midy
        global clicked_first, clicked_tile, ctiles, clicked_x
        global clicked_y, mine_placement
        clicked_first = False
        welcometext.pack_forget()
        Difficulty = level
        if Difficulty == "easy":
            grid_size = [9, 9, 10, 10]
        elif Difficulty == "medium":
            grid_size = [16, 16, 40, 40]
        elif Difficulty == "hard":
            grid_size = [21, 21, 99, 99]
        flags = grid_size[3]
        flags_label.configure(text=f"Flags remaining: {flags}")
        mines = grid_size[2]
        width = grid_size[0]
        height = grid_size[1]
        creategrid()

        easyframe.pack_forget()
        midframe.pack_forget()
        hardframe.pack_forget()

    def mine_placement():
        """Place mines on grid."""
        global clicked_first, clicked_tile
        global surrounding, ctiles, clicked_x, clicked_y
        if clicked_first:
            clicked_x = clicked_tile[0]
            clicked_y = clicked_tile[1]

            ctiles = [(clicked_x - 1, clicked_y - 1),
                      (clicked_x, clicked_y - 1),
                      (clicked_x + 1, clicked_y - 1),
                      (clicked_x - 1, clicked_y),
                      (clicked_x + 1, clicked_y),
                      (clicked_x - 1, clicked_y + 1),
                      (clicked_x, clicked_y + 1),
                      (clicked_x + 1, clicked_y + 1)]
            for i in range(mines):
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                while (
                    x,
                    y) in Mine_list or (
                    x,
                    y) == (
                    clicked_x,
                    clicked_y) or (
                    x,
                        y) in ctiles:
                    x = random.randint(0, width - 1)
                    y = random.randint(0, height - 1)
                Mine_list.append((x, y))
                surrounding.append((x - 1, y - 1))
                surrounding.append((x, y - 1))
                surrounding.append((x + 1, y - 1))
                surrounding.append((x + 1, y))
                surrounding.append((x - 1, y))
                surrounding.append((x - 1, y + 1))
                surrounding.append((x, y + 1))
                surrounding.append((x + 1, y + 1))
                if (x, y) in surrounding:
                    surrounding.remove((x, y))
                for x, y in surrounding:
                    if x < 0 or y < 0 or x > width or y > height:
                        surrounding.remove((x, y))

    # Difficulty Buttons

    easyframe = Frame(tkmine)
    easyframe.pack(padx=10, pady=10)
    easyframe.config(bg="#f8f8f8")
    midframe = Frame(tkmine)
    midframe.pack(padx=10, pady=10)
    midframe.config(bg="#f8f8f8")
    hardframe = Frame(tkmine)
    hardframe.pack(padx=10, pady=10)
    hardframe.config(bg="#f8f8f8")
    easy = Button(
        easyframe,
        text="Easy",
        bg="#f8f8f8",
        font=btnfont,
        width=6,
        command=lambda: set_difficulty("easy"))
    easy.pack(padx=10, pady=10, side="left")
    easytext = Label(
        easyframe,
        text="9x9 Grid with 10 Mines",
        bg="#f8f8f8",
        font=textfont)
    easytext.pack(side="left")
    medium = Button(
        midframe,
        text="Medium",
        bg="#f8f8f8",
        font=btnfont,
        width=6,
        command=lambda: set_difficulty("medium"))
    medium.pack(padx=10, pady=10, side="left")
    midtext = Label(
        midframe,
        text="16x16 Grid with 40 Mines",
        bg="#f8f8f8",
        font=textfont)
    midtext.pack(side="left")
    hard = Button(
        hardframe,
        text="Hard",
        bg="#f8f8f8",
        font=btnfont,
        width=6,
        command=lambda: set_difficulty("hard"))
    hard.pack(padx=10, pady=10, side="left")
    hardtext = Label(
        hardframe,
        text="21x21 Grid with 99 mines",
        bg="#f8f8f8",
        font=textfont)
    hardtext.pack(padx=10, pady=10, side="left")
    easyspeed = Label(
        easyframe,
        text=f"Fastest Time: {easytime}s",
        font=textfont,
        bg="#f8f8f8")
    mediumspeed = Label(
        midframe,
        text=f"Fastest Time: {mediumtime}s",
        font=textfont,
        bg="#f8f8f8")
    hardspeed = Label(
        hardframe,
        text=f"Fastest Time: {hardtime}s",
        font=textfont,
        bg="#f8f8f8")
    if easytime > 0:
        easyspeed.pack(side='left', padx=10)
    if mediumtime > 0:
        mediumspeed .pack(side='left', padx=10)
    if hardtime > 0:
        hardspeed .pack(side='left', padx=10)
    buttons = {}

    def creategrid():
        """Create grid for game."""
        global start, flags, mines, width, height, frame
        start = time.time()
        frame = tk.Frame(
            tkmine,
            cursor='target',
            height=500,
            width=500,
            bg="#f8f8f8")
        frame.pack(side="top", padx=20, pady=20)
        frame.grid_propagate(False)
        for x in range(height):
            frame.grid_rowconfigure(x, weight=1)

        for y in range(width):
            frame.grid_columnconfigure(y, weight=1)
        tile_size = 10
        for x in range(height):
            for y in range(width):

                b = Button(
                    frame,
                    text=" ",
                    bg="lightgrey",
                    fg="black",
                    font=btnfont)
                b.config(width=tile_size, height=tile_size)
                b.grid_propagate(False)

                b.grid(row=height - 1 - x, column=y, sticky="nsew")

                buttons[(x, y)] = b
                b.bind("<Button-1>", lambda event, x=x, y=y: onclick(x, y))
                b.bind(
                    "<Button-3>",
                    lambda event,
                    x=x,
                    y=y: onrightclick(x, y))
    flagged = []

    def onrightclick(x, y):
        """Set how rightclick works."""
        global flags, mines, width, height, Game_overMS

        if Game_overMS != 2:
            global flags
            if (x, y) in revealed:
                print("Tile already revealed")
            elif (x, y) in Mine_list and (x, y) in flagged:
                mines += 1
                print(f"Flag removed at ({x},{y})")
                flags += 1
                flags_label.config(text=f"Flags remaining: {flags}")
                buttons[(x, y)].config(text=" ", bg="lightgrey")
                flagged.remove((x, y))
            elif (x, y) in Mine_list:
                mines -= 1
                flags -= 1
                flags_label.config(text=f"Flags remaining: {flags}")
                print(f"Placed flag at ({x},{y})")
                buttons[(x, y)].config(text="⚑", bg="lightgrey")
                flagged.append((x, y))
                if mines == 0:
                    Game_overMS = 1
                    Game_Over()
            elif (x, y) in flagged:
                print(f"Flag removed at ({x},{y})")
                buttons[(x, y)].config(text=" ", bg="lightgrey")
                flagged.remove((x, y))
                flags += 1
                flags_label.config(text=f"Flags remaining: {flags}")
            elif flags > 0:
                print(f"Placed flag at ({x},{y})")
                buttons[(x, y)].config(text="⚑", bg="lightgrey")
                flagged.append((x, y))
                flags -= 1
                flags_label.config(text=f"Flags remaining: {flags}")
            elif flags == 0:
                print("No flags remaining!")
    revealed = set()
# recursion stuff

    def reveal(x, y):
        """Recursively reveal mines."""
        if (x, y) in Mine_list or (x, y) in revealed:
            return
        number = surrounding.count((x, y))

        display_number = number if number != 0 else ""
        mscolours = [
            "blue",
            "green",
            "red",
            "darkblue",
            "darkred",
            "cyan",
            "black",
            "grey"]
        if display_number != "":
            buttons[(x, y)].config(text=display_number,
                                   bg="white",
                                   fg=mscolours[display_number - 1])
        else:
            buttons[(x, y)].config(text="", bg="white")
        revealed.add((x, y))
        if number == 0:
            surroundingtiles = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                                (x - 1, y), (x + 1, y),
                                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
            for (a, b) in surroundingtiles:
                if 0 <= a <= width - 1 and 0 <= b <= height - 1:
                    reveal(a, b)

    def onclick(x, y):
        """Set how click works."""
        global Game_overMS, clicked_first, clicked_tile
        text.configure(text="")
        if not clicked_first:
            clicked_first = True
            clicked_tile = (x, y)
            mine_placement()
        if Game_overMS != 2:
            print(f"Button ({x},{y}) clicked")
            if (x, y) in flagged:
                print(
                    "Flag alr there. Remove before revealing")
                return
            if (x, y) in Mine_list:
                buttons[(x, y)].config(text="💥", bg="red")
                Game_overMS = 2
                Game_Over()
                print("You hit a mine! Game Over!")
                return
            if clicked_first:
                reveal(x, y)

    def destroy():
        """Destroy tkinter."""
        tkmine.destroy()

    def play():
        """Play the game."""
        easyframe.pack(padx=10, pady=10)
        midframe.pack(padx=10, pady=10)
        hardframe.pack(padx=10, pady=10)

    def reset_game():
        """Reset the game."""
        global Game_overMS
        flags_label.config(text=f"{username}, Try Another Difficulty!")
        Game_overMS = 1
        surrounding.clear()
        Mine_list.clear()
        revealed.clear()
        flagged.clear()
        try:
            frame.destroy()
        except BaseException:
            pass
        try:
            btnsframe.destroy()
        except BaseException:
            pass
        play()

    def yesno():
        """Create buttons for yes and no."""
        global text
        global btnsframe
        flags_label.config(text=f"Would you like to play again {username}? ")
        frame.pack_forget()
        btnsframe = Frame(tkmine, bg="#f8f8f8")
        btnsframe.pack()
        Btnyes = Button(
            btnsframe,
            text="Yes",
            width=6,
            bg="#f8f8f8",
            font=btnfont,
            command=reset_game)
        Btnyes.pack(side="left", padx=10, pady=10)
        Btnno = Button(
            btnsframe,
            text="No",
            width=6,
            bg="#f8f8f8",
            font=btnfont,
            command=destroy)
        Btnno.pack(side="left", padx=10, pady=10)

    def Game_Over():
        """Display game over screen."""
        global easytime, mediumtime, hardtime, Game_overMS, frame
        global end, start, text, height, width
        if Game_overMS == 2:
            for (x, y) in Mine_list:
                buttons[(x, y)].config(text="💥", bg="red")
                if (x, y) in flagged:
                    buttons[(x, y)].config(text="⚑", bg="orange")
            flags_label.config(text=f"You hit a Mine! Game Over!")
            tkmine.after(2000, yesno)

        elif Game_overMS == 1:

            end = time.time()
            times = end - start
            times = round(times, 2)
            if width == 9 and height == 9:
                if easytime == 0 or times < easytime:
                    easytime = times
                    easyspeed.config(text=f"Fastest Time: {easytime}s")
                    easyspeed.pack(side='left', padx=10)
            if width == 16 and height == 16:
                if mediumtime == 0 or times < mediumtime:
                    mediumtime = times
                    mediumspeed.config(text=f"Fastest Time: {mediumtime}s")
                    mediumspeed.pack(side='left', padx=10)

            if width == 21 and height == 21:
                if hardtime == 0 or times < hardtime:
                    hardtime = times
                    hardspeed.config(text=f"Fastest Time: {hardtime}s")
                    hardspeed.pack(side='left', padx=10)
            print(times)
            flags_label.config(
                text=f"You completed Minesweeper - Easy in {times} seconds!")
            timed.append(times)

            for (x, y) in Mine_list:
                buttons[(x, y)].config(text="🌱", bg="#8eef8c")
            tkmine.after(2000, yesno)

            print("Congratulations! You found all the mines!")
    tkmine.mainloop()
