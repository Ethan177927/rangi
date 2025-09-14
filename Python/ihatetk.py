
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

# 'Grid' Taken from https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/
  for row in range(1):
    for col in range(1):
        tk.Button(
            tkmain,
            text=f"Cell ({row}, {col})",
            width=10,
            height=5,
        ).grid(row=row, column=col)

  tkmain.mainloop()
tk_window()
