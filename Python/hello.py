options = ["easy", "medium", "hard"]
Difficulty = ""
grid_size = [0,0,0,0]
Mine_list = []
surrounding = []
import random
Game_overMS = False
import rpsminus1
import minesweeper


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

if Game_chosen == "1":
  rpsminus1.rps_game()
if Game_chosen == "3":
  minesweeper.minesweeper_game()