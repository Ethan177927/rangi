options = ["easy", "medium", "hard"]
Difficulty = ""
grid_size = [0,0,0,0]
Mine_list = []
surrounding = []
import random
Game_overMS = False
rps_scores = {}
rpscontinue = True

account_create = input("Would you like to create an account to save your progress? \n 1: Yes \n 2: No\n").lower()

while account_create not in ["1","2"]:
  account_create = input("Invalid input. Please enter 1 for Yes or 2 for No: ").lower()
if account_create == "1":
  username = input("Enter a username: ")
  password = input("Enter a password: ")
  usernamedictionary = {}
  if username not in usernamedictionary:
    usernamedictionary[username] = password
  else:
    print("Username already exists. Please try again.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
""" Somehow stores this dictionary in a file so that it can be accessed later. """

print("Game compendium \n 1: Rock, Paper, Scissors Minus \n 2: Visual Memory Test \n 3: Minesweeper")
rps_streak = 0
Game_chosen = input("Choose a game by entering the corresponding number: ")
while Game_chosen not in ["1","2","3"]:
  Game_chosen = input("Invalid Input. Please enter 1, 2, or 3 to choose a game: ")
if Game_chosen == "1":
  print("Welcome to Game 1 of the Compendium: Rock, Paper, Scissors Minus One!")
  print("To play this game, enter rock, paper or scissors to make your choice.")
  options = ["rock", "paper", "scissors"]


if Game_chosen == "3":
  print("Welcome to Game 3 of the Compendium: Minesweeper!")
  print("To play this game, enter a difficulty level")
  print("Easy: 9x9 grid with 10 mines")
  print("Medium: 16x16 grid with 40 mines")
  print("Hard: 20x24 grid with 99 mines")

  if Difficulty not in options:
    Difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()

  if Difficulty == "easy":
    grid_size = [9,9,10,10]
  if Difficulty == "medium":
    grid_size = [16,16,40,40]
  if Difficulty == "hard":
    grid_size = [20,24,99,99]

  flags = grid_size[3]
  mines = grid_size[2]
  width = grid_size[0]
  height = grid_size[1]


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
  for x,y in Mine_list:
    table[height-y][x] = 9
  for x,y in surrounding:
    if table[height-y][x] != 9:
      table[height-y][x] += 1
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
    while action != "flag" and action != "reveal":
      action = input("Invalid action. Please enter 'flag' or 'reveal': ")

    Guess = (x,y)
    print(Guess)
    if action == 'flag':
      for row in table:
        if Guess in row:
          flags -= 1
          row[row.index(Guess)] = 'F'
    print("Flags remaining: " + str(flags))

    if action == "reveal":
      if Guess in Mine_list:
        print("You hit a mine! Game Over!")
        for row in table:
          for mine in Mine_list:
            for x,y in Mine_list:
              table[height-y][x] = 9
        Game_overMS = True
    for row in table:
      print(row)