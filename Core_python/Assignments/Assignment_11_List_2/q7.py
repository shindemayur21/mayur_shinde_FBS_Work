# 7. Python Program to Find the Intersection of Two Lists

li = [3, 5, 2, 6, 7]
li2 = [98, 6, 54, 23, 5]

li3 = []

for i in li:
    if i in li2:
        li3.append(i)

print("Intersection of lists:", li3)
