import tkinter as tk
from tkinter import *

height = -1
def minesweeper_game():
  global flags
  global mines
  global width
  global height
  tkmine = tk.Tk() 
  tkmine.configure(bg = "#f8f8f8")


  # Fonts
  titlefont = ("Helvetica Neue", 30, "bold")
  textfont = ("Helvetica Neue", 15)
  Btnfont = ("Helvetica", 12, "bold")



  titlemine = Label(tkmine, text = "Minesweeper", font = titlefont, fg = "black", bg = "#f8f8f8")
  titlemine.pack(padx = 10, pady = 10)


  screen_width = tkmine.winfo_screenwidth()
  screen_height = tkmine.winfo_screenheight()

  # found off of google to get the screenheigth and width of the user's screen.
  swidth = int(screen_width/2 - 850/2)
  sheight = int(screen_height/2 - 650/2)

  # sets size of the window and the +swidth and +sheight are x,y values for where the window opens on the screen.
  tkmine.geometry(f"850x650+{swidth}+{sheight}")


  Mine_list = []
  surrounding = []
  import random 
  global Game_overMS
  Game_overMS = 1
  flags = 0
  flags_label = Label(tkmine, text = f"Flags remaining: {flags} ", font = textfont, bg = "#f8f8f8")
  flags_label.pack(padx = 10, pady = 10)
  def set_difficulty(level):    
    global Difficulty
    global grid_size
    global flags
    global mines
    global width
    global height
    Difficulty = level
    if Difficulty == "easy":
      grid_size = [8,8,10,10]
    elif Difficulty == "medium":
      grid_size = [15,15,40,40]  
    elif Difficulty == "hard":
      grid_size = [20,20,99,99]
     
    flags = grid_size[3]
    flags_label.configure(text = f"Flags remaining: {flags}")
    mines = grid_size[2]
    width = grid_size[0]
    height = grid_size[1] 
    easy.pack_forget()
    medium.pack_forget()
    hard.pack_forget()
    easyframe.pack_forget()
    midframe.pack_forget()
    hardframe.pack_forget()
    text = Label(tkmine, text = "Left click to reveal a tile, right click to place/remove a flag.", font = textfont, bg = "#f8f8f8")
    text.pack(padx = 10)

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
    createGrid()


  # Difficulty Buttons

  easyframe = Frame(tkmine)
  easyframe.pack (padx = 10, pady = 10)
  easyframe.config(bg = "#f8f8f8")
  midframe = Frame(tkmine)
  midframe.pack(padx = 10, pady = 10)
  midframe.config(bg = "#f8f8f8")
  hardframe = Frame(tkmine)
  hardframe.pack(padx = 10, pady = 10)
  hardframe.config(bg = "#f8f8f8")
  easy = Button(easyframe, text = "Easy", bg = "#f8f8f8", font = Btnfont, width = 6, command = lambda: set_difficulty("easy"))
  easy.pack(padx = 10, pady = 10, side = "left")
  easytext = Label (easyframe, text = "9x9 Grid with 10 Mines", bg = "#f8f8f8", font = textfont)
  easytext.pack(side = "left")
  medium = Button(midframe, text = "Medium",bg = "#f8f8f8", font = Btnfont, width = 6, command = lambda: set_difficulty("medium"))
  medium.pack(padx = 10, pady = 10, side = "left")
  midtext = Label(midframe, text = "16x16 Grid with 40 Mines",bg = "#f8f8f8", font = textfont )
  midtext.pack(side = "left")
  hard = Button(hardframe, text = "Hard",bg = "#f8f8f8", font = Btnfont, width = 6, command = lambda: set_difficulty("hard"))
  hard.pack(padx = 10, pady = 10, side = "left")
  hardtext = Label(hardframe, text = "21x21 Grid with 99 mines", bg = "#f8f8f8",font = textfont)
  hardtext.pack(padx = 10, pady = 10, side = "left")
  
  buttons = {}
  def createGrid():
    global flags
    global mines
    global width
    global height
    frame = tk.Frame(tkmine, cursor = 'target')
    frame.pack(fill = "both", expand = True, side = "top", padx = 20, pady = 20)
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
    global mines
    global width
    global height
    global Game_overMS
    if Game_overMS != 2:
      global flags
      if (x,y) in revealed:
        print("This tile has already been revealed, you cannot place a flag here.")
      elif (x,y) in Mine_list and (x,y) in flagged:
        mines +=1         
        print(f"Flag removed at ({x},{y})")
        flags += 1
        flags_label.config(text = f"Flags remaining: {flags}")
        buttons[(x,y)].config(text = " ", bg = "lightgrey")
        flagged.remove((x,y))
      elif (x,y) in Mine_list:
        mines -= 1
        flags -=1 
        flags_label.config(text = f"Flags remaining: {flags}")
        print(f"Placed flag at ({x},{y})")
        buttons[(x,y)].config(text = "⚑", bg = "lightgrey")
        flagged.append((x,y))
        if mines == 0:
          Game_overMS = 2
          Game_Over()
      elif (x,y) in flagged:
        print(f"Flag removed at ({x},{y})")
        buttons[(x,y)].config(text = " ", bg = "lightgrey")
        flagged.remove((x,y))
        flags +=1
        flags_label.config(text = f"Flags remaining: {flags}")
      elif flags > 0:
        print(f"Placed flag at ({x},{y})")
        buttons[(x,y)].config(text = "⚑", bg = "lightgrey")
        flagged.append((x,y))
        flags -= 1
        flags_label.config(text = f"Flags remaining: {flags}")
      elif flags == 0:
        print("No flags remaining!")
  revealed = set()
 # recursion stuff
  def reveal(x,y):
    if (x,y) in Mine_list or (x,y) in revealed:
      return
    number = surrounding.count((x,y))

    display_number = number if number != 0 else ""
    mscolours = ["blue", "green", "red", "darkblue", "darkred", "cyan", "black", "grey"]
    if display_number != "":
      buttons[(x,y)].config(text = display_number, bg = "white", fg = mscolours[display_number-1])
    else:
      buttons[(x,y)].config(text = "", bg = "white")
    revealed.add((x,y))

    if number == 0:
      surroundingtiles = [(x-1,y-1), (x,y-1), (x+1,y-1),
                          (x-1,y),           (x+1,y),
                          (x-1,y+1), (x,y+1), (x+1,y+1)]
      for (a,b) in surroundingtiles:
        if 0 <= a <= width-1 and 0 <= b <= height-1:
          reveal(a,b)

  def onClick(x,y):
    global Game_overMS
    if Game_overMS != 2:
      print(f"Button ({x},{y}) clicked")
      if (x,y) in flagged:
        print("There is a flag there, please remove it before revealing the tile.")
        return
      if (x,y) in Mine_list:
        buttons[(x,y)].config(text = "💥", bg = "red")
        Game_overMS = 2
        Game_Over()
        print("You hit a mine! Game Over!")
        return
      reveal(x,y)
  def Game_Over():
    global Game_overMS
    if Game_overMS == 2:
      for (x,y) in Mine_list:
        buttons[(x,y)].config(text = "💥", bg = "red")

    elif Game_overMS == 1:  
      for (x,y) in Mine_list:
        if (x,y) not in flagged:
          buttons[(x,y)].config(text = "💥", bg = "red")
      print("Congratulations! You found all the mines!")
  tkmine.mainloop()
minesweeper_game()
"""
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
"""

