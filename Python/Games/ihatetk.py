"""Main Menu with the name entry."""


import tkinter as tk
from tkinter import *

# Fonts
titlefont = ("Helvetica Neue", 30, "bold")
textfont = ("Helvetica Neue", 15)
btnfont = ("Helvetica", 12, "bold")
gamefont = ("Helvetica", 15, "bold")


def tk_window():
    """Create tk window."""
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

    # background colour
    name_var = tk.StringVar()
    name_label = Label(
        tkmain,
        text='Enter your name: ',
        font=btnfont,
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

    def pack_buttons():
        """Pack the buttons of the games."""
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
            command=vmt_game)
        vmt.grid(row=2, column=0, padx=10, pady = 10)

    def submit():
        """Get username from user."""
        name = name_var.get()
        print(name)
        with open("usernames.txt", "a") as f:
            if name != "" and len(name) < 20:
                f.write(name + "\n")
                hidden_label.config(text='Username saved!', fg="green")
                tkmain.after(1500, hide_username)
            else:
                print("Invalid Username.")
                hidden_label.config(text='Invalid Input or Username exists.')

    sub_btn = tk.Button(
        tkmain,
        text='Submit',
        command=submit,
        font=btnfont,
        bg="#efedef")
    sub_btn.pack(padx=10, pady=10)

    def hide_username():
        """Hide buttons."""
        name_label.pack_forget()
        name_entry.pack_forget()
        sub_btn.pack_forget()
        hidden_label.pack_forget()
        pack_buttons()


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

    def vmt_game():
        """Open Visual Memory Test."""
        print("visual Memory Test opening...")
        tkmain.destroy()
        import visualmemorytest
        visualmemorytest.vmt()

    tkmain.mainloop()


tk_window()
