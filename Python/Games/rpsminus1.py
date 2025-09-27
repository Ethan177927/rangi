import random 
import tkinter as tk
from tkinter import * 

player_choice = []
options = ["rock", "paper", "scissors"]
computer_option = []

def rps_game():
  rps1 = Tk()
  rps1.geometry("900x600")
  rps1.configure(bg="lightgrey")
  rps1.title("Rock Paper Scissors Minus")
  title = Label(rps1, text="Rock Paper Scissors Minus One", font=("Roman", 30), bg = "lightgrey")
  title.pack(padx = 10, pady = 40)
  
  
  computer_option.append(random.choice(options))
  computer_option.append(random.choice(options))
  if computer_option[0] == computer_option[1]:
    while computer_option[0] == computer_option[1]:
      computer_option[1] = random.choice(options)

  def check():
    if len(player_choice) == 2:
      for i in range(3):
        if options[i] in player_choice:
          pass
        else:
          buttons[i].pack_forget()
      print("You chose: " + player_choice[0] + " and " + player_choice[1])

      

  def pick(choice, button):
    player_choice.append(choice)
    print(choice)
    button.pack_forget()
    check()



  def play():
    print("Playing RPS-1")
    play_btn.pack_forget()
    player_choice.clear()
    for button in buttons:
      button.pack(padx = 10, pady = 10, side = "left")
    

  play_btn = tk.Button(rps1, text = 'Play', command = play, width = 25, height = 10, font = ("Roman", 20), bg = "white", fg = "black")
  play_btn.pack(padx = 10, pady = 10)
  framerps = Frame(rps1, bg = "lightgrey")
  framerps.pack(pady = 20)

  rockbtn = tk.Button(framerps, text = 'Rock', command=lambda: pick("rock", rockbtn), width = 15, height = 5, font = ("Roman", 15), bg = "white", fg = "black")
  paperbtn = tk.Button(framerps, text = 'Paper', command = lambda: pick("paper", paperbtn), width = 15, height = 5, font = ("Roman", 15), bg = "white", fg = "black")
  scissorbtn = tk.Button(framerps, text = 'Scissors', command = lambda: pick("scissors", scissorbtn), width = 15, height = 5, font = ("Roman", 15), bg = "white", fg = "black")
  
  buttons = [rockbtn, paperbtn, scissorbtn]

  rps1.mainloop()

rps_game()
'''
    minesweep.pack(padx = 10, pady = 10, side  = "left")
    rps.pack(padx = 10, pady = 10, side = "left")  
    vmt.pack(padx = 10, pady = 10, side = "left")
    leaderboard.pack(padx = 10, pady = 20)




    

  def minesweeper():
    print("Minesweeper opening...")
  def rps():
    print("Rock Paper Scissors opening...")
  def vmt():
    print("visual Memory Test opening...")
  row_frame = Frame(tkmain)
  row_frame.pack(pady = 10)

  minesweep = tk.Button(row_frame, text="Minesweeper", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3, command = minesweeper)  
  rps = tk.Button(row_frame, text="Rock Paper Scissors", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3, command = rps)
  vmt = tk.Button(row_frame, text="Visual Memory Test", font=("Roman", 20), bg = "white", fg = "black", width = 20, height = 3, command = vmt)









  rps_scores = {}
  rpscontinue = True
  player_choice = []
  options = ["rock", "paper", "scissors"]
  rps_streak = 0
  while rpscontinue == True:
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

      remove = input(player_choice[0]+ " or " + player_choice[1] + ", which do you want to remove? ").lower()
      while remove not in player_choice:
        remove = input(f"Invalid input. Please choose one of your options to remove: {player_choice[0], player_choice[1]} ").lower()
      player_choice.remove(remove)
      cremove = random.choice(computer_option)
      computer_option.remove(cremove)

      print("You chose to remove: " + remove)
      print("The computer chose to remove: " + cremove)
      print("You are left with: " + player_choice[0] + "!\n" + "The computer is left with: " + computer_option[0] + "!")

      if player_choice[0] == computer_option[0]:
        print("It's a tie!")
      elif (player_choice[0] == "rock" and computer_option[0] == "scissors") or (player_choice[0] == "scissors" and computer_option[0] == "paper") or (player_choice[0] == "paper" and computer_option[0] == "rock"):
        print("You Win!")
        rps_streak += 1
      else:
        print("You Lose!")
        rps_streak = 0
      print("Your current win streak is: " + str(rps_streak))

      rpscontinue = int(input("Would you like to continue playing? \nIf you leave now then your score will be scored \n1: Yes \n2: No\n"))
      while rpscontinue not in [1,2]:
        rpscontinue = int(input("Invalid input.\n1: Yes\n2: No\n"))
      if rpscontinue == 2:
        rpscontinue = False
        print("Thanks for playing!")
        if rps_streak > 0:
            print("Your final score is: " + str(rps_streak))
            print("Your scores have been saved as follows: " + str(rps_scores))
        else:
            print("You have no score to save. Better luck next time!")
rps_game()
'''