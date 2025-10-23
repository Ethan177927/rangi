# random testing document, not part of assignment



options = ["easy", "medium", "hard"]
Difficulty = ""
grid_size = [0,0,0,0]
Mine_list = []
surrounding = []
Game_overMS = False
import tkinter as tk
import rpsminus1
import visualmemorytest
import ihatetk
import minesweeper

ihatetk.tk_window()




username = input("Enter a username: ")
password = input("Enter a password: ")
usernamedictionary = {}
if username not in usernamedictionary:
  usernamedictionary[username] = password
else:
  print("Username already exists. Please try again.")
  while username in usernamedictionary:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
  usernamedictionary[username] = password
""" Somehow stores this dictionary in a file so that it can be accessed later. """

print("Game compendium \n 1: Rock, Paper, Scissors Minus \n 2: Visual Memory Test \n 3: Minesweeper")
Game_chosen = input("Choose a game by entering the corresponding number: ")
while Game_chosen not in ["1","2","3"]:
  Game_chosen = input("Invalid Input. Please enter 1, 2, or 3 to choose a game: ")


if Game_chosen == "1":
  rpsminus1.rps_game()
if Game_chosen == "2":
  visualmemorytest.vmt()
if Game_chosen == "3":
  minesweeper.minesweeper_game()