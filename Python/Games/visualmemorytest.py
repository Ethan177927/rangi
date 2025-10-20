
import tkinter as tk
from tkinter import *
import time
import random
import subprocess

def vmt():
    global sqaures
    global height
    global width


    tkvmt = tk.Tk()
    tkvmt.title("Visual Memory Test")
    global game_overvmt
    game_overvmt = 1

   # bg = "#f8f8f8"
    # Fonts
    titlefont = ("Helvetica Neue", 30, "bold")
    textfont = ("Helvetica Neue", 15)
    Btnfont = ("Helvetica", 12, "bold")

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

    def backMenus():
        tkvmt.destroy()
        subprocess.run(["python", r"Python\Games\ihatetk.py"])

    BackMenu = Button(
        tkvmt,
        text="Back To Menu",
        bg="#f8f8f8",
        font=Btnfont,
        command=backMenus)
    BackMenu.pack(padx=10, pady=10, side="bottom", anchor='w')


    
    diff = Frame(tkvmt, bg = '#f8f8f8')
    diff.pack(padx = 10, pady = 10)
    def easy():
        global height
        global width
        global timeto
        global starttime
        height = 4
        width = 4
        timeto = 20
        starttime = timeto
        diff.pack_forget()
        start()
        createGrid()


    def medium():
        global height
        global starttime
        global width
        global timeto
        height = 6
        width = 6
        timeto = 30
        starttime = timeto
        diff.pack_forget()
        start()
        createGrid()


    def hard():
        global height
        global width
        global starttime
        global timeto
        height = 8
        width = 8
        timeto = 60
        starttime = timeto
        diff.pack_forget()
        start()
        createGrid()



        
    easydiff = Button(diff, text = "Easy Mode", bg = '#f8f8f8', font = Btnfont, command = easy)
    easydiff.pack(padx = 10, pady = 10, side = 'left')
    mediumdiff = Button(diff, text = "Medium Mode", bg = '#f8f8f8', font = Btnfont, command = medium)
    mediumdiff.pack(padx = 10, pady = 10, side = 'left')
    harddiff = Button(diff, text = "Hard Mode", bg = "#f8f8f8", font = Btnfont, command = hard)
    harddiff.pack(padx = 10, pady = 10, side = 'left')
    
  
    def start():
        global squares
        squares = []
        math = int(height * width / 3)
        while len(squares) < math:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pos = (x, y)
            squares.append(pos)

    def set_state(state):
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

    global one
    one = 0
    def countdown(timeto):
        global current_time
        current_time = timeto
        print(current_time)
        time_label = Label(text = f"Time Remaining: {timeto} seconds", font = textfont, bg = '#f8f8f8')
        time_label.pack()
        def count():
            nonlocal timeto
            global current_time
            current_time = timeto

            if game_overvmt != 1:
                time_label.pack_forget()
                return
            elif timeto > 0:
                timeto -= 1
                time_label.config(text = f"Time Remaining: {timeto} seconds")
                time_label.after(1000, count)
            
            else:
                set_state(2)
                time_label.pack_forget()
        count()
    def onClick(x, y):
        global game_overvmt
        global one
        global finish
        

        if game_overvmt != 1:
            return

        if (x, y) != squares[one]:
            set_state(2)
        elif (x, y) == squares[one]:
            if one < len(squares) - 1:
                one += 1
                print('g')
            elif one == len(squares) - 1:
                finish = starttime - current_time

                set_state(3)
        else:
            if (x, y) in squares:
                buttons[(x, y)].configure(text="X", bg="red")
                

    def createGrid():
        global height
        global width
        global frame
        frame = tk.Frame(tkvmt, width=1000, height=1000, cursor='target')
        frame.pack(side="top", padx=20, pady=20)
        frame.pack_propagate(False) 
        for x in range(height):
            frame.grid_rowconfigure(x, weight=1, uniform="row")

        for y in range(width):
            frame.grid_columnconfigure(y, weight=1, uniform="column")

        for x in range(height):
            for y in range(width):
                b = Button(
                    frame,
                    text=" ",
                    font=Btnfont,
                    bg="#f8f8f8",
                    fg="black",
                    height = 20,
                    width = 20
                    )
                b.grid(row=height - 1 - x, column=y, sticky="nsew") 
                buttons[(x, y)] = b
                b.config(state = "disabled")

        tkvmt.after(1000, delay)
       
    def delay():
        change_colours()

    def change_colours(num=0):
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
                    b.bind("<Button-1>", lambda event, x=x, y=y: onClick(x, y))
            countdown(timeto)


    def button_break():
        global frame
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
            
            textl = Label(
                tkvmt,
                text='You won! Would you like to play again?',
                font=textfont,
                bg='#f8f8f8')
            if finish > 1:
                text2 = Label(tkvmt, text = f'You took {finish} seconds to complete the game!', font = textfont, bg = '#f8f8f8')
            else:
                text2 = Label(tkvmt, text = f'You took {finish} second to complete the game!', font = textfont, bg = '#f8f8f8')
            text2.pack(pady = 10, padx = 10)
        else:
            textl = Label(
                tkvmt,
                text = "Unknown Error Occured.",
                font=textfont,
                bg='#f8f8f8')
        textl.pack(padx = 10, pady = 10)

        def again():
            tkvmt.destroy()
            vmt()
        btnframes474 = Frame(tkvmt, bg='#f8f8f8')
        btnframes474.pack(pady=10, padx=10)
        btnplay = Button(
            btnframes474,
            text='Play Again',
            bg='#f8f8f8',
            width=10,
            font=Btnfont,
            command=again)
        btnplay.pack(side='left', padx=10, pady=10)

        def destroy():
            tkvmt.destroy()
            import ihatetk
            ihatetk

        btnquit = Button(
            btnframes474,
            text='Quit',
            font=Btnfont,
            width=10,
            bg='#f8f8f8',
            command=destroy)

        btnquit.pack(side='left', padx=10, pady=10)
   # tkmine.destroy()

# lambda creates an anonymous function thing
# had to do the num = 0 num + 1 thing or else it does all of the colours
# changes at once and it doesnt load colours properly



    tkvmt.mainloop()
vmt()

"""
with open("usernames.txt", "a") as f:
            if name != "" and name not in open("usernames.txt").read():
                f.write(name + "\n")
                hidden_label.config(text='Username saved!', fg="green")
                tkmain.after(2000, hide_username)
            else:
                print("Invalid Username.")
                hidden_label.config(text='Invalid Input or Username exists.')
                
                """
'''
finish = 3
with open("leaderboardvmt.txt", "a") as f:
        username = open("usernames.txt").read().strip().splitlines()[-1]
        if username not in open("leaderboardvmt.txt").read():
            f.write(f"{username}: {finish} seconds\n")

            '''