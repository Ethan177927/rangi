options = ["easy", "medium", "hard"]
Difficulty = ""
grid_size = [0,0,0,0]
Mine_list = []
surrounding = []
import random

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


print(Mine_list)
print(surrounding)

print("In order to select the location you want to reveal or place a flag, enter the coordinates in the format: x,y,flag/reveal")

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

if Guess in Mine_list and action == "reveal":
  print("You hit a mine! Game Over!")
