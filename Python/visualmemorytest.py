

def vmt():
  Grid = []

  rows = int(input("Enter the number of rows: "))
  columns = int(input("Enter the number of columns: "))
  import random
  import time
  height = rows
  width = columns

  # Copied from Minesweeper file that i made ecayse i was too lazt to code
  table = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(0)
    table.append(row)
  for row in table:
    print(row)


  hidden = int((height*width)/3)
  score = 0
  print(hidden)
  hiddentable = table
  hiddens = []
  for i in range(hidden):
    x = random.randint(0,width-1)
    y = random.randint(0,height-1)
    if hiddentable[y][x] == 1:
      i -= 1
    else:
      hiddentable[y][x] = 1
      hiddens.append((x,y))

  for row in hiddentable:
    print(row)

  time.sleep(3)
  print("\n"*400)

  for row in table:
    print(row)

  print("Where are the hidden squares?")
