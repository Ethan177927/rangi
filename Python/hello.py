options = ["easy", "medium", "hard"]
Difficulty = ""
grid_size = [0,0,0,0]
Mine_list = []
surrounding = []
import random
Game_over = False

print("Game compendium \n 1: Rock, Paper, Scisssors Minus \n 2: Visual Memory Test \n 3: Minesweeper")
rps_streak = 0
Game_chosen = input("Choose a game by entering the corresponding number: ")
while Game_chosen not in ["1","2","3"]:
  Game_chosen = input("Invalid Input. Please enter 1, 2, or 3 to choose a game: ")
if Game_chosen == "1":
  print("Welcome to Game 1 of the Compendium: Rock, Paper, Scissors Minus!")
  print("To play this game, enter rock, paper or scissors to make your choice.")
  options = ["rock", "paper", "scissors"]
  player_choice = []
  first_option = input("Enter your choice: ").lower()
  while first_option not in options:
    first_option = input("Invalid input. Please enter rock, paper or scissors: ").lower()
  player_choice.append(first_option)
  second_option = input("Enter your second choice: ").lower()
  while second_option not in options:
    second_option = input("Invalid input. Please enter rock, paper or scissors: ").lower()
  player_choice.append(second_option)
  computer_option = []
  computer_option.append(random.choice(options))
  computer_option.append(random.choice(options))
  if computer_option[0] == computer_option[1]:
    while computer_option[0] == computer_option[1]:
      computer_option[1] = random.choice(options)
  print("You chose: " + player_choice[0] + " and " + player_choice[1])
  print("The computer chose: " + computer_option[0] + " and " + computer_option[1])
  print("You will now choose to remove one of your choices and the computer will do the same.")
  remove = input(player_choice[0]+ "or " + player_choice[1] + ", which do you want to remove? ").lower()
  while remove not in player_choice:
    remove = input(f"Invalid input. Please choose one of your options to remove: {player_choice[0], player_choice[1]} ").lower()
  player_choice.remove(remove)
  cremove = random.choice(computer_option)
  computer_option.remove(cremove)
  print("You chose to remove: " + remove)
  print("The computer chose to remove: " + cremove)

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
      row.append((j,9-i))
    table.append(row)
  for row in table:
    print(row)

  str(j)+","+ str(9-i)
  print("In order to select the location you want to reveal or place a flag, enter the coordinates in the format: x,y,flag/reveal")

  while Game_over == False:
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
          flags -=1
          row[row.index(Guess)] = "F"
    for row in table:
      print(row)
    print("Flags remaining: " + str(flags))

    if action == "reveal":
      if Guess in Mine_list:
        print("You hit a mine! Game Over!")
        for row in table:
          for mine in Mine_list:
            if mine in row:
              row[row.index(mine)] = "X"
    for row in table:
      print(row)
