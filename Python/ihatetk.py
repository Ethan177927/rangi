
import tkinter as tk
from tkinter import * 


def tk_window():
  tkmain = tk.Tk()

 # sets title
  tkmain.title("Alston Games Comependium")

  # sets size
  tkmain.geometry("750x650")

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
      else:
        print("a")
        hidden_label.config(text = 'Invalid Input or Username exists.')

      
  sub_btn = tk.Button(tkmain, text = 'Submit', command = submit)
  sub_btn.pack(padx = 10, pady = 10)

  def minesweeper():
    print("minesweeper opening...")
    



  minesweep = tk.Button(tkmain, text="Minesweeper", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3, command = minesweeper)
  minesweep.pack(padx = 10, pady = 10)
  


  rps = tk.Button(tkmain, text="Rock Paper Scissors", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3)
  rps.pack(padx = 10, pady = 10)  


  vmt = tk.Button(tkmain, text="Visual Memory Test", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3)
  vmt.pack(padx = 10, pady = 10)


  tkmain.mainloop()
tk_window()
