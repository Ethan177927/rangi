
import tkinter as tk
from tkinter import * 


def tk_window():
  tkmain = tk.Tk()

 # sets title
  tkmain.title("Alston Games Comependium")


  screen_width = tkmain.winfo_screenwidth()
  screen_height = tkmain.winfo_screenheight()

  # found off of google to get the screenheigth and width of the user's screen.
  swidth = int(screen_width/2 - 850/2)
  sheight = int(screen_height/2 - 650/2)

  # sets size of the window and the +swidth and +sheight are x,y values for where the window opens on the screen.
  tkmain.geometry(f"850x650+{swidth}+{sheight}")


  # creates the title of the game.
  title = Label(tkmain, text="Alston Games Compendium", font=("Roman", 30), bg = "lightgrey")
  title.pack(padx = 10, pady = 40)

  # background colour
  tkmain.configure(bg="lightgrey")
  name_var=tk.StringVar()
  name_label = Label(tkmain, text = 'Enter your name: ', font =("Roman", 15), bg = "lightgrey")
  name_entry = Entry(tkmain, textvariable = name_var, font =("Roman", 15), bg = "white", fg = "black", width = 30)
  hidden_label = Label(tkmain, text = '', bg = "lightgray", font = ("Roman", 15), fg = "red")
  hidden_label.pack()
  name_label.pack(padx = 10, pady = 10)
  name_entry.pack(padx = 10, pady = 10)
  def submit():
    name = name_var.get()
    print(name)
    with open("usernames.txt", "a") as f:
      if name != "" and name not in open("usernames.txt").read():
        f.write(name + "\n")
        hidden_label.config(text = 'Username saved!', fg = "green")
        tkmain.after(5000, hide_username)
      else:
        print("a")
        hidden_label.config(text = 'Invalid Input or Username exists.')

      
  sub_btn = tk.Button(tkmain, text = 'Submit', command = submit)
  sub_btn.pack(padx = 10, pady = 10)

  def hide_username():
    name_label.pack_forget()
    name_entry.pack_forget()
    sub_btn.pack_forget()
    hidden_label.pack_forget()
    minesweep.pack(padx = 10, pady = 10, side  = "left")
    rps.pack(padx = 10, pady = 10, side = "left")  
    vmt.pack(padx = 10, pady = 10, side = "left")
    leaderboard.pack(padx = 10, pady = 20)




    

  def minesweeper():
    print("Minesweeper opening...")
  def rps():
    print("Rock Paper Scissors opening...")
  def vmt():
    print("visual Memory Test opening...")
  row_frame = Frame(tkmain)
  row_frame.pack(pady = 10)

  minesweep = tk.Button(row_frame, text="Minesweeper", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3, command = minesweeper)  
  rps = tk.Button(row_frame, text="Rock Paper Scissors", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3, command = rps)
  vmt = tk.Button(row_frame, text="Visual Memory Test", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3, command = vmt)

  leaderboard = Label(tkmain, text = "Leaderboard", font = ("Roman", 25), bg = "lightgrey")


  tkmain.mainloop()
tk_window()
