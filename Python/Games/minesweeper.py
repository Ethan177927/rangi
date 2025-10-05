import tkinter as tk
from tkinter import *
height = -1
def minesweeper_game():  
  tkmine = tk.Tk() 
  tkmine.title("Minesweeper")

  screen_width = tkmine.winfo_screenwidth()
  screen_height = tkmine.winfo_screenheight()

  # found off of google to get the screenheigth and width of the user's screen.
  swidth = int(screen_width/2 - 850/2)
  sheight = int(screen_height/2 - 650/2)

  # sets size of the window and the +swidth and +sheight are x,y values for where the window opens on the screen.
  tkmine.geometry(f"850x650+{swidth}+{sheight}")
  




  options = ["easy", "medium", "hard"]
  Difficulty = ""
  grid_size = [0,0,0,0]
  Mine_list = []
  surrounding = []
  import random
  Game_overMS = False

  print("Welcome to Game 3 of the Compendium: Minesweeper!")
  print("To play this game, enter a difficulty level")
  print("Easy: 9x9 grid with 10 mines")
  print("Medium: 16x16 grid with 40 mines")
  print("Hard: 21x21 grid with 99 mines")

  while Difficulty not in options:
    Difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()

  if Difficulty == "easy":
    grid_size = [8,8,10,10]
  elif Difficulty == "medium":
    grid_size = [15,15,40,40]
  elif Difficulty == "hard":
    grid_size = [20,20,99,99]
  global flags

  flags = grid_size[3]
  mines = grid_size[2]
  width = grid_size[0]
  height = grid_size[1]
  
  buttons = {}
  def createGrid():
    frame = tk.Frame(tkmine)
    frame.pack(fill = "both", expand = True, side = "top")
    for x in range(height):
      frame.grid_rowconfigure(x, weight = 1, uniform = "row")

    for y in range(width):
      frame.grid_columnconfigure(y,  weight = 1, uniform = "column")

    for x in range (height):
      for y in range (width):
        b = Button(frame, text = " ", bg = "lightgrey", fg = "black")
        b.grid(row = height-1-x, column = y, sticky = "nsew") 

        buttons[(x,y)] = b
        b.bind("<Button-1>", lambda event, x=x, y=y: onClick(x,y))
        b.bind("<Button-3>", lambda event, x=x, y=y: onRightClick(x,y))
  flagged = []

  def onRightClick(x,y):
    global flags
    if (x,y) in revealed:
      print("This tile has already been revealed, you cannot place a flag here.")
    elif (x,y) in flagged:
      print(f"Flag removed at ({x},{y})")
      buttons[(x,y)].config(text = " ", bg = "lightgrey")
      flagged.remove((x,y))
      flags +=1
    elif flags > 0:
      print(f"Placed flag at ({x},{y})")
      buttons[(x,y)].config(text = "F", bg = "yellow")
      flagged.append((x,y))
      flags -= 1
    elif flags == 0:
      print("No flags remaining!")

  revealed = set()
 # recursion stuff
  def reveal(x,y):
    if (x,y) in Mine_list or (x,y) in revealed:
      return
    number = surrounding.count((x,y))

    display_number = number if number > 0 else ""
    buttons[(x,y)].config(text = display_number, bg = "white")

    revealed.add((x,y))
    if number == 0:
      surroundingtiles = [(x-1,y-1), (x,y-1), (x+1,y-1),
                          (x-1,y),           (x+1,y),
                          (x-1,y+1), (x,y+1), (x+1,y+1)]
      for (a,b) in surroundingtiles:
        if 0 <= a <= width-1 and 0 <= b <= height-1:
          reveal(a,b)

  def onClick(x,y):
    print(f"Button ({x},{y}) clicked")
    if (x,y) in flagged:
      print("There is a flag there, please remove it before revealing the tile.")
      return
    if (x,y) in Mine_list:
      buttons[(x,y)].config(text = "X", bg = "red")
      Game_overMS = True
      print("You hit a mine! Game Over!")
      return
    reveal(x,y)



  createGrid()
  
  for i in range(mines):
    x = random.randint(0,width-1)
    y = random.randint(0,height-1)
    if (x,y) in Mine_list:
      i -= 1
    else:
      Mine_list.append((x,y))
      surrounding.append((x-1,y-1))
      surrounding.append((x,y-1))
      surrounding.append((x+1,y-1))
      surrounding.append((x+1,y))
      surrounding.append((x-1,y))
      surrounding.append((x-1,y+1))
      surrounding.append((x,y+1))
      surrounding.append((x+1,y+1))
      if (x,y) in surrounding:
        surrounding.remove((x,y))
      for x,y in surrounding:
        if x<0 or y<0 or x> width or y > height:
          surrounding.remove((x,y))
    
  print(Mine_list)
  print(surrounding)

  table = []
  for i in range(height+1):
    row = []
    for j in range(width+1):
      row.append(0)
    table.append(row)

  for row in table:
    print(row)

  str(j)+","+ str(height-i)
  print("In order to select the location you want to reveal or place a flag, enter the coordinates in the format: x,y,flag/reveal")
  print("The first 'tile' is (0,0) which is the bottom left corner of the grid. The top right corner is (" + str(width) + "," + str(height) + ")")
  while Game_overMS == False:
    Guess = input("Guess: ").split(",")
    print(Guess)
    x = int(Guess[0])
    while x > width or x<0:
      x = int(input("Invalid x co-ordinate. Please enter a value between 0 and "+ str(width)+ ": "))
    y = int(Guess[1])
    while y > height or y<0:
      y = int(input("Invalid y co-ordinate. Please enter a value between 0 and "+ str(height)+ ": ")) 
    action = Guess[2]
    while action not in ['flag','reveal']:
      action = input("Invalid action. Please enter 'flag' or 'reveal': ")
  

    Guess = (x,y)
    print(Guess)
    if action == 'flag':
      if flags == 0:
        print("You have no flags remaining!")
        continue
      if table[height-y][x] == 8:
        print("There is already a flag there, it will now be removed and be added back to your flag count.")
        flags += 1
        if (x,y) in Mine_list:
          table[height-y][x] = 9
        elif (x,y) in surrounding:
            number = surrounding.count((x,y))
            table[height-y][x] = number
        else:
          table[height-y][x] = 0
      else:
        table[height-y][x] = 8
        flags -= 1
      print("Flags remaining: " + str(flags))
      for row in table:
        print(row)

    Guess = (x,y)
    if action == "reveal":
      if Guess in Mine_list:
        print("You hit a mine! Game Over!")
        Game_overMS = True
        for (x,y) in Mine_list:
          table[height-y][x] = 9
      elif Guess in surrounding:
        print("washed")
        number = surrounding.count((x,y))
        table[height-y][x] = number
      else:
        table[height-y][x] = 7
        surroundingsafe = []
        surroundingsafe.append((x-1,y-1))
        surroundingsafe.append((x,y-1))
        surroundingsafe.append((x+1,y-1))
        surroundingsafe.append((x+1,y))
        surroundingsafe.append((x-1,y))
        surroundingsafe.append((x-1,y+1))
        surroundingsafe.append((x,y+1))
        surroundingsafe.append((x+1,y+1))
        for (x,y) in surroundingsafe:
          if x < 0 or y < 0 or x > width or y > height or (x,y) in Mine_list or (x,y) in surrounding:
            surroundingsafe.remove((x,y))
        for (x,y) in surroundingsafe:
          table[height-y][x] = 7
      for row in table:
        print(row)
  tkmine.mainloop()

minesweeper_game()