

def vmt():
  Grid = []
  if redo != 1:
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    import random
    import time
    global height
    global width
    height = rows
    width = columns
  elif redo == 1:
    height +=1
    width +=1
    print("The grid size has increase by 1 row and 1 column. The new grid size is " + str(height) + " rows and " + str(width) + " columns.")
  # Copied from Minesweeper file that i made ecayse i was too lazt to code
  table = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(0)
    table.append(row)
  for row in table:
    print(row)


  hiddens = []
  for i in range(height):
    hidden_row = []
    for j in range(width):
      hidden_row.append(0)
    hiddens.append(hidden_row)

  hidden = int((height*width)/3)
  print(hidden)
  for i in range(hidden):
    x = random.randint(0,width-1)
    y = random.randint(0,height-1)
    if hiddens[y][x] == 1:
      i -= 1
    else:
      hiddens[y][x] = 1
      hiddens.append((x+1,y+1))

  for hidden_row in hiddens:
    print(hidden_row)

  time.sleep(3)
  print("\n"*400)

  for row in table:
    print(row)

  print("Where are the hidden squares? The bottom left corner is (1,1) and the top right corner is " + str(width) + "," + str(height) + ".")


  for i in range(hidden):
    try:
      x = int(input("Enter x-coordinate: "))
    except ValueError:
      x = int(input("Invalid input. Please enter a number for the x-coordinate: "))
    try:
      y = int(input("Enter y-coordinate: "))
    except ValueError:
      y = int(input("Invalid input. Please enter a number for the y-coordinate: "))
    if hiddens[y-1][x-1] ==1:
      print("That is Correct!")
      hidden -=1
    else:
      print("That is Incorrect!")
      
    
  if hidden == 0:
    print("You managed to find all the hiddens. Would you like to play again?")
    global score
    score +=1
    replay = input("1: Yes \n2: No\n")
    while replay not in ["1","2"]:
      replay = input("Invalid input. Please enter 1 for Yes or 2 for No: \n")
    if replay == "1":
      redo = 1
      vmt()

    else:
      print("Thank you for playing!")
  #saves score to a file
