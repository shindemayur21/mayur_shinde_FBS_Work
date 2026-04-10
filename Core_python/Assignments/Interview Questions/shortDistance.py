# Find the shortest distance a person moving in different directions

path = "wwsennwwwwwn"

x = 0
y = 0

for i in path:
    if i == 'e':
        x = x + 1  #if person moves to the East
    elif i == 'w':
        x = x-1    #if person moves to the West
    elif i == 'n':
        y = y+1    #if person moves to the North
    elif i == 's':
        y = y-1    #if person moves to the South
    else:
        print("Invalid direction")

dist = ((x**2) * (y**2)) ** 0.5

print(f'Shortest distance is : {dist}')
