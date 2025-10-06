
import tkinter as tk
from tkinter import *
import time

def vmt():
  tkvmt = tk.Tk()
  tkvmt.title("Visual Memory Test")
  screen_width = tkvmt.winfo_screenwidth()
  screen_height = tkvmt.winfo_screenheight()
  swidth = int(screen_width/2 - 850/2)
  sheight = int(screen_height/2 - 650/2)
  tkvmt.geometry(f"850x650+{swidth}+{sheight}")  
  tkvmt.configure(bg="lightgrey")
  title = Label(tkvmt, text="Visual Memory Test", font=("Roman", 30), bg = "lightgrey")
  title.pack(padx = 10, pady = 40)

  height = 3
  width = 3
  def createGrid():
    frame = tk.Frame(tkvmt, width =400, height = 400, cursor = 'target')
    frame.pack(fill = "both", expand = True, side = "top", padx = 20, pady = 20)
    for x in range(height):
      frame.grid_rowconfigure(x, weight = 1, uniform = "row")

    for y in range(width):
      frame.grid_columnconfigure(y,  weight = 1, uniform = "column")

    for x in range (height):
      for y in range (width):
        b = Button(frame, text = " ", bg = "lightgrey", fg = "black")
        b.grid(row = height-1-x, column = y, sticky = "nsew") 
  createGrid()
  tkvmt.mainloop()
vmt()