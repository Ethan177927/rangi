def minesweeper_game():  
  options = ["easy", "medium", "hard"]
  Difficulty = ""
  grid_size = [0,0,0,0]
  Mine_list = []
  surrounding = []
  import random
  Game_overMS = False
  import rpsminus1

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
      for row in table:
        print(row)

    if action == "reveal":
      if Guess in Mine_list:
        print("You hit a mine! Game Over!")
        for row in table:
          for mine in Mine_list:
            for x,y in Mine_list:
              table[height-y][x] = 9
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
        if (x,y) in Mine_list or (x,y) in surrounding:
          surroundingsafe.remove((x,y))
        for (a,b) in surroundingsafe:
          if a<0 or b<0 or a> width or b > height:
            surroundingsafe.remove((a,b))
        for (a,b) in surroundingsafe:
          if (a,b) not in Mine_list and (a,b) not in surrounding:
            table[height-b][a] = 7
        for row in table:
          print(row)
        Game_overMS = True