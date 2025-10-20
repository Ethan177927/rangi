'''Minesweeper Game in Python using Tkinter'''

import tkinter as tk
from tkinter import *
import time
import subprocess
timed = []
# py -m autopep8 --in-place --aggressive --aggressive C:\Users\ethan\OneDrive\Documents\GitHub\rangi\Python\Games\minesweeper.py

height = -1
easytime = 0
mediumtime = 0
hardtime= 0

def minesweeper_game():
    global flags, mines, width, height
    tkmine = tk.Tk()
    tkmine.configure(bg="#f8f8f8")

    # Fonts
    titlefont = ("Helvetica Neue", 30, "bold")
    textfont = ("Helvetica Neue", 15)
    Btnfont = ("Helvetica", 12, "bold")

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

    def BackMenus():
        tkmine.destroy()
        subprocess.run(["python", r"Python\Games\ihatetk.py"])

    BackMenu = Button(
        tkmine,
        text="Back To Menu",
        bg="#f8f8f8",
        font=Btnfont,
        command=BackMenus)
    BackMenu.pack(padx=10, pady=10, side="bottom", anchor='w')

    global text
    text = Label(
        tkmine,
        text=f"Left click to reveal a tile, right click to place/remove a flag.",
        font=textfont,
        bg="#f8f8f8")
    text.pack(padx=10)

    def set_difficulty(level):
        global Difficulty, grid_size, flags, mines, width, height, midx, midy
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
        mid = (round(width / 2), round(height / 2))
        print(mid)
        midx = mid[0]
        midy = mid[1]
        easyframe.pack_forget()
        midframe.pack_forget()
        hardframe.pack_forget()
        surroundingmid = [(midx - 1, midy - 1), (midx, midy - 1), (midx + 1, midy - 1),
                          (midx - 1, midy), (midx + 1, midy),
                          (midx - 1, midy + 1), (midx, midy + 1), (midx + 1, midy + 1)]
        for i in range(mines):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            while (x, y) in Mine_list or (x, y) == (midx, midy) or (x, y) in surroundingmid:
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
        createGrid()

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
        font=Btnfont,
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
        font=Btnfont,
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
        font=Btnfont,
        width=6,
        command=lambda: set_difficulty("hard"))
    hard.pack(padx=10, pady=10, side="left")
    hardtext = Label(
        hardframe,
        text="21x21 Grid with 99 mines",
        bg="#f8f8f8",
        font=textfont)
    hardtext.pack(padx=10, pady=10, side="left")
    easyspeed =  Label(easyframe, text = f"Fastest Time: {easytime}s", font = textfont, bg = "#f8f8f8")
    mediumspeed =  Label(midframe, text = f"Fastest Time: {mediumtime}s", font = textfont, bg = "#f8f8f8")
    hardspeed =  Label(hardframe, text = f"Fastest Time: {hardtime}s", font = textfont, bg = "#f8f8f8")
    if easytime != 0:
        easyspeed.pack(side = 'left', padx = 10)
    if mediumtime != 0:
        mediumspeed .pack(side = 'left', padx = 10)
    if hardtime != 0:
        hardspeed .pack(side = 'left', padx = 10)
    buttons = {}

    def createGrid():
        global start, flags, mines, width, height, frame
        start = time.time()
        frame = tk.Frame(tkmine, cursor='target', height=5, width=5)
        frame.pack(fill="both", expand=True, side="top", padx=20, pady=20)
        for x in range(height):
            frame.grid_rowconfigure(x, weight=1, uniform="row")

        for y in range(width):
            frame.grid_columnconfigure(y, weight=1, uniform="column")

        for x in range(height):
            for y in range(width):
                b = Button(
                    frame,
                    text=" ",
                    bg="lightgrey",
                    fg="black",
                    height=2,
                    width=4,
                    font=Btnfont)
                b.grid(row=height - 1 - x, column=y, sticky="nsew")

                buttons[(x, y)] = b
                b.bind("<Button-1>", lambda event, x=x, y=y: onClick(x, y))
                b.bind(
                    "<Button-3>",
                    lambda event,
                    x=x,
                    y=y: onRightClick(x,y))
        buttons[(midx, midy)].config(bg="lightyellow")
    flagged = []

    def onRightClick(x, y):
        global flags, mines, width, height, Game_overMS

        if Game_overMS != 2:
            global flags
            if (x, y) in revealed:
                print(
                    "This tile has already been revealed, you cannot place a flag here.")
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
                                   bg="white", fg=mscolours[display_number - 1])
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

    def onClick(x, y):
        global Game_overMS
        text.pack_forget()

        if Game_overMS != 2:
            print(f"Button ({x},{y}) clicked")
            if (x, y) in flagged:
                print(
                    "There is a flag there, please remove it before revealing the tile.")
                return
            if (x, y) in Mine_list:
                buttons[(x, y)].config(text="💥", bg="red")
                Game_overMS = 2
                Game_Over()
                print("You hit a mine! Game Over!")
                return
            reveal(x, y)

    def destroy():
        tkmine.destroy()
    def play():
        easyframe.pack(padx=10, pady=10)
        midframe.pack(padx=10, pady=10)
        hardframe.pack(padx=10, pady = 10)

    def reset_game():
        global Game_overMS
        print('egg')
        Game_overMS = 1
        surrounding.clear()
        Mine_list.clear()
        revealed.clear()
        flagged.clear()
        try:
            frame.destroy()
        except:
            pass
        try:
            btnsframe.destroy()
        except:
            pass
        play()

            




    def yesno():
        global text
        global btnsframe
        flags_label.config(text="Would you like to play again?")
        frame.pack_forget()
        btnsframe = Frame(tkmine, bg="#f8f8f8")
        btnsframe.pack()
        Btnyes = Button(
            btnsframe,
            text="Yes",
            width=6,
            bg="#f8f8f8",
            font=Btnfont,
            command=reset_game)
        Btnyes.pack(side="left", padx=10, pady=10)
        Btnno = Button(
            btnsframe,
            text="No",
            width=6,
            bg="#f8f8f8",
            font=Btnfont,
            command=destroy)
        Btnno.pack(side="left", padx=10, pady=10)

    def Game_Over():
        global easytime, mediumtime, hardtime, Game_overMS, frame, end, start, text, height, width
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
            if width == 9 and height ==9:
                if easytime == 0 or times < easytime:
                    easytime = times
            if width == 16 and height ==16:
                if mediumtime == 0 or times < mediumtime:
                    mediumtime = times
            if width == 21 and height ==21:
                if hardtime == 0 or times < hardtime:
                    hardtime = times
            print(times)
            flags_label.config(
                text=f"You completed Minesweeper - Easy in {times} seconds!")
            timed.append(times)

            for (x, y) in Mine_list:
                buttons[(x, y)].config(text="🌱", bg="#8eef8c")
            tkmine.after(2000, yesno)

            print("Congratulations! You found all the mines!")
    tkmine.mainloop()
minesweeper_game()