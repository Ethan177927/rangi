
import tkinter as tk
from tkinter import *
import time
import random

def vmt():
  global sqaures
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
  swidth = int(screen_width/2 - 850/2)
  sheight = int(screen_height/2 - 650/2)
  tkvmt.geometry(f"850x650+{swidth}+{sheight}")  
  tkvmt.configure(bg = "#f8f8f8")
  title = Label(tkvmt, text="Visual Memory Test", font =  titlefont, bg = "#f8f8f8")
  title.pack(padx = 10, pady = 40)

  height = int(input("Height: "))
  width = int(input("Width: "))
  
  def start():
    global squares
    squares = []
    math = int(height*width/3)
    for i in range (math):
      x = random.randint(0,width-1)
      y = random.randint(0,height-1)
      if (x,y) in squares:
        i -= 1
      else:
        squares.append((x,y))
    print(squares)
    
  def createGrid():
    frame = tk.Frame(tkvmt, width =400, height = 400, cursor = 'target')
    frame.pack(fill = "both", expand = True, side = "top", padx = 20, pady = 20)
    for x in range(height):
      frame.grid_rowconfigure(x, weight = 1, uniform = "row")

    for y in range(width):
      frame.grid_columnconfigure(y,  weight = 1, uniform = "column")

    for x in range (height):
      for y in range (width):
        b = Button(frame, text = " ", font = Btnfont, bg = "#f8f8f8", fg = "black")
        b.grid(row = height-1-x, column = y, sticky = "nsew")
        buttons[(x,y)] = b
        b.bind("<Button-1>", lambda event, x=x, y=y: onClick(x,y))
  def change_colours():
    global squares
    for (x,y) in squares:
      buttons[(x,y)].configure(bg = "cyan")
      time.sleep(0.5)
      buttons[(x,y)].configure(bg = "gray")

  createGrid()
  start()
  change_colours()

  
  tkvmt.mainloop()


  def onClick(x,y):
    global game_overvmt
    if game_overvmt == 2:
      game_over()

  def game_over():
    print('a')


vmt()