"""My fantastic Digi Tech Game that I definitely had fun making!!!!!!!"""


import tkinter as tk
from tkinter import *
  
'''
py -m pip install autopep8
'''

# Fonts
titlefont = ("Helvetica Neue", 30, "bold")
textfont = ("Helvetica Neue", 15)
Btnfont = ("Helvetica", 12, "bold")


def tk_window():
    tkmain = tk.Tk()

   # sets title
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

    # background colour
    name_var = tk.StringVar()
    name_label = Label(
        tkmain,
        text='Enter your name: ',
        font=Btnfont,
        bg="#f8f8f8")
    name_entry = Entry(
        tkmain,
        textvariable=name_var,
        font=textfont,
        bg="#efeded",
        fg="black",
        width=30)
    hidden_label = Label(
        tkmain,
        text='',
        bg="#f8f8f8",
        font=textfont,
        fg="red")
    hidden_label.pack()
    name_label.pack(padx=10, pady=10)
    name_entry.pack(padx=10, pady=10)
    global name

    def submit():
        name = name_var.get()
        print(name)
        with open("usernames.txt", "a") as f:
            if name != "" and name not in open("usernames.txt").read():
                f.write(name + "\n")
                hidden_label.config(text='Username saved!', fg="green")
                tkmain.after(2000, hide_username)
            else:
                print("Invalid Username.")
                hidden_label.config(text='Invalid Input or Username exists.')

    sub_btn = tk.Button(
        tkmain,
        text='Submit',
        command=submit,
        font=Btnfont,
        bg="#efedef")
    sub_btn.pack(padx=10, pady=10)

    def hide_username():
        name_label.pack_forget()
        name_entry.pack_forget()
        sub_btn.pack_forget()
        hidden_label.pack_forget()
        minesweep.pack(padx=10, pady=10, side="left")
        rps.pack(padx=10, pady=10, side="left")
        vmt.pack(padx=10, pady=10, side="left")
        leaderboard.pack(padx=10, pady=20)

    def minesweepers():
        print("Minesweeper opening...")
        import minesweeper
        tkmain.destroy()
        minesweeper.minesweeper_game()

    def rpsgame():
        print("Rock Paper Scissors opening...")
        import rpsminus1
        tkmain.destroy()
        rpsminus1.rps_game()

    def vmt():
        print("visual Memory Test opening...")
        import visualmemorytest
        tkmain.destroy()
        visualmemorytest.vmt()
    row_frame = Frame(tkmain, bg='#f8f8f8')
    row_frame.pack(pady=10)

    minesweep = tk.Button(
        row_frame,
        text="Minesweeper",
        font=Btnfont,
        bg="#f8f8f8",
        fg="black",
        width=20,
        height=3,
        command=minesweepers)
    rps = tk.Button(
        row_frame,
        text="Rock Paper Scissors",
        font=Btnfont,
        bg="#f8f8f8",
        fg="black",
        width=20,
        height=3,
        command=rpsgame)
    vmt = tk.Button(
        row_frame,
        text="Visual Memory Test",
        font=Btnfont,
        bg="#f8f8f8",
        fg="black",
        width=20,
        height=3,
        command=vmt)

    leaderboard = Label(
        tkmain,
        text="Leaderboard",
        font=textfont,
        bg="#f8f8f8")

    tkmain.mainloop()


tk_window()
