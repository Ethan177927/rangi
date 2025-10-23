"""Visual Memory Test Game created using Tkinter."""

import tkinter as tk
from tkinter import *
import random
import subprocess

easytime = 0
mediumtime = 0
hardtime = 0


def vmt():
    """Visual Memory Test Game."""
    global squares, height, width, timeto, starttime, one, game_overvmt
    global username

    try:
        with open("usernames.txt", "r") as f:
            lines = f.readlines()
            username = lines[-1].strip()
    except FileNotFoundError:
        username = "Player"
    print(username)

    tkvmt = tk.Tk()
    tkvmt.title("Visual Memory Test")
    game_overvmt = 1
    one = 0
    # Fonts
    titlefont = ("Helvetica Neue", 30, "bold")
    textfont = ("Helvetica Neue", 15)
    btnfont = ("Helvetica", 12, "bold")
    buttons = {}
    screen_width = tkvmt.winfo_screenwidth()
    screen_height = tkvmt.winfo_screenheight()
    swidth = int(screen_width / 2 - 850 / 2)
    sheight = int(screen_height / 2 - 650 / 2)
    tkvmt.geometry(f"850x650+{swidth}+{sheight}")
    tkvmt.configure(bg="#f8f8f8")
    title = Label(
        tkvmt,
        text="Visual Memory Test",
        font=titlefont,
        bg="#f8f8f8")
    title.pack(padx=10, pady=40)

    def backmenus():
        """Back Button Function for Visual Memory Test."""
        tkvmt.destroy()
        subprocess.run(["python", r"Python\Games\menu2.py"])

    welcometext = Label(
        tkvmt,
        text=f"Welcome {username} to a Memory test!",
        font=textfont,
        bg="#f8f8f8")
    welcometext.pack(padx=10, pady=10)

    BackMenu = Button(
        tkvmt,
        text="Back To Menu",
        bg="#f8f8f8",
        font=btnfont,
        command=backmenus)
    BackMenu.pack(padx=10, pady=10, side="bottom", anchor='w')

    diff = Frame(tkvmt, bg='#f8f8f8')
    diff.pack(padx=10, pady=10)
    scores = Frame(tkvmt, bg='#f8f8f8')
    scores.pack(pady=5)

    def easy():
        """Set Easy Difficulty for Visual Memory Test."""
        global height, width, timeto, starttime
        height = 4
        width = 4
        timeto = 20
        starttime = timeto
        diff.pack_forget()
        scores.pack_forget()
        start()
        creategrid()

    def medium():
        """Set Medium Difficulty for Visual Memory Test."""
        global height, starttime, width, timeto
        height = 6
        width = 6
        timeto = 30
        starttime = timeto
        diff.pack_forget()
        scores.pack_forget()
        start()
        creategrid()

    def hard():
        """Set Hard Difficulty for Visual Memory Test."""
        global height, width, starttime, timeto
        height = 8
        width = 8
        timeto = 60
        starttime = timeto
        diff.pack_forget()
        scores.pack_forget()
        start()
        creategrid()

    easydiff = Button(diff,
                      text="Easy Mode",
                      bg='#f8f8f8',
                      font=btnfont,
                      command=easy)
    easydiff.pack(padx=10, pady=10, side='left')
    if easytime > 0:
        easylabel = Label(
            scores,
            text=f"Easy Best Time: {easytime} seconds",
            font=textfont,
            bg='#f8f8f8')
        easylabel.pack(padx=5)
    mediumdiff = Button(diff,
                        text="Medium Mode",
                        bg='#f8f8f8',
                        font=btnfont,
                        command=medium)
    mediumdiff.pack(padx=10, pady=10, side='left')
    if mediumtime > 0:
        mediumlabel = Label(
            scores,
            text=f"Medium Best Time: {mediumtime} seconds",
            font=textfont,
            bg='#f8f8f8')
        mediumlabel.pack(padx=5)
    harddiff = Button(diff,
                      text="Hard Mode",
                      bg="#f8f8f8",
                      font=btnfont,
                      command=hard)
    harddiff.pack(padx=10, pady=10, side='left')
    if hardtime > 0:
        hardlabel = Label(
            scores,
            text=f"Hard Best Time: {hardtime} seconds",
            font=textfont,
            bg='#f8f8f8')
        hardlabel.pack(padx=5)

    def start():
        """Start Visual Memory Test Game. Creates Squares to be memorized."""
        global squares
        squares = []
        math = int(height * width / 3)
        while len(squares) < math:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pos = (x, y)
            squares.append(pos)

    def set_state(state):
        """Set Game State for Visual Memory Test."""
        global game_overvmt
        global winloss
        if state == 2:
            winloss = 2
            game_overvmt = 0
            print(winloss)
            button_break()
        elif state == 3:
            winloss = 3
            game_overvmt = 0
            button_break()

    def countdown(timeto):
        """Countdown Timer for Visual Memory Test."""
        global current_time
        current_time = timeto
        print(current_time)
        time_label = Label(text=f"Time Remaining: {timeto} seconds",
                           font=textfont,
                           bg='#f8f8f8')
        time_label.pack()

        def count():
            """Start countdown timer for vmt."""
            nonlocal timeto
            global current_time
            current_time = timeto
            if game_overvmt != 1:
                time_label.pack_forget()
                return
            elif timeto > 0:
                timeto -= 1
                time_label.config(text=f"Time Remaining: {timeto} seconds")
                time_label.after(1000, count)
            else:
                set_state(2)
                time_label.pack_forget()
        count()

    def onclick(x, y):
        """On Click Function for Visual Memory Test."""
        global game_overvmt, one, finish
        if game_overvmt != 1:
            return
        if (x, y) != squares[one]:
            set_state(2)
        elif (x, y) == squares[one]:
            if one < len(squares) - 1:
                one += 1
            elif one == len(squares) - 1:
                finish = starttime - current_time
                set_state(3)
        else:
            if (x, y) in squares:
                buttons[(x, y)].configure(text="X", bg="red")

    def creategrid():
        """Create Grid for Visual Memory Test."""
        welcometext.pack_forget()
        global height, width, frame
        frame = tk.Frame(tkvmt, width=500, height=500, cursor='target')
        frame.pack(side="top", padx=20, pady=20)
        frame.propagate(False)

        for x in range(height):
            frame.grid_rowconfigure(x, weight=1)
        for y in range(width):
            frame.grid_columnconfigure(y, weight=1)
        for x in range(height):
            for y in range(width):
                b = Button(
                    frame,
                    text=" ",
                    font=btnfont,
                    bg="#f8f8f8",
                    fg="black",
                    height=20,
                    width=20
                    )
                b.grid(row=height - 1 - x, column=y, sticky="nsew")
                buttons[(x, y)] = b
                b.config(state="disabled")
        tkvmt.after(1000, delay)

    def delay():
        """Delay Function for Visual Memory Test."""
        change_colours()

    def change_colours(num=0):
        """Change Colours of Squares to be memorized in Visual Memory Test."""
        global squares
        if num < len(squares):
            x, y = squares[num]
            buttons[(x, y)].configure(bg="cyan")
            tkvmt.after(1000, lambda: buttons[(x, y)].configure(bg="#f8f8f8"))
            tkvmt.after(1200, lambda: change_colours(num + 1))
        else:
            for button in buttons.values():
                button.config(state="normal")
            for x in range(height):
                for y in range(width):
                    b = buttons[(x, y)]
                    b.bind("<Button-1>", lambda event, x=x, y=y: onclick(x, y))
            countdown(timeto)

    def button_break():
        """End Visual Memory Test Game and Displays Result."""
        global frame, text2, textl, btnAframe, finish, height, width
        global easytime, mediumtime, hardtime
        print('break')
        print(winloss)
        frame.pack_forget()
        if winloss == 2:
            textl = Label(
                tkvmt,
                text='You lost! Would you like to play again?',
                font=textfont,
                bg='#f8f8f8')
        elif winloss == 3:
            if finish > 1:
                if height == 4 and width == 4:
                    easytime = finish
                elif height == 6 and width == 6:
                    mediumtime = finish
                elif height == 8 and width == 8:
                    hardtime = finish
                text2 = Label(tkvmt,
                              text=f'You took {finish} seconds '
                              'to complete the game!',
                              font=textfont,
                              bg='#f8f8f8')
            else:
                text2 = Label(tkvmt,
                              text=f'You took {finish} second '
                              'to complete the game!',
                              font=textfont,
                              bg='#f8f8f8')
            text2.pack(pady=10, padx=10)
            textl = Label(
                tkvmt,
                text='You won! Would you like to play again?',
                font=textfont,
                bg='#f8f8f8')
        else:
            textl = Label(
                tkvmt,
                text="Unknown Error Occured.",
                font=textfont,
                bg='#f8f8f8')
        textl.pack(padx=10, pady=10)

        def restart():
            """Restart Visual Memory Test Game."""
            global winloss, frame, finish, current_time
            global one, btnAframe, game_overvmt
            winloss = 0
            finish = 0
            one = 0
            current_time = 0
            game_overvmt = 1
            squares.clear()
            try:
                frame.destroy()
            except BaseException:
                pass
            try:
                btnAframe.destroy()
            except BaseException:
                pass
            try:
                text2.destroy()
            except BaseException:
                pass
            try:
                textl.destroy()
            except BaseException:
                pass
            try:
                scores.destroy()
            except BaseException:
                pass
            diff.pack()

        btnAframe = Frame(tkvmt, bg='#f8f8f8')
        btnAframe.pack(pady=10, padx=10)
        btnplay = Button(
            btnAframe,
            text='Play Again',
            bg='#f8f8f8',
            width=10,
            font=btnfont,
            command=restart)
        btnplay.pack(side='left', padx=10, pady=10)

        def destroy():
            """Quits Visual Memory Test Game."""
            tkvmt.destroy()
            subprocess.run(["python", r"Python\Games\menu2.py"])

        btnquit = Button(
            btnAframe,
            text='Quit',
            font=btnfont,
            width=10,
            bg='#f8f8f8',
            command=destroy)
        btnquit.pack(side='left', padx=10, pady=10)
    tkvmt.mainloop()
