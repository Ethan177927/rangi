
great = []
total = 0
x = ''
three = [3]


N = input("N: ")
for num in range(int(N)+1):
  x += str(num)

for egg in range(len(x)):
  if int(x[egg]) in three:
    total +=1    
  
print(total)


