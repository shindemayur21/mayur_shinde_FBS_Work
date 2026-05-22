# 6. Python Program to Find the Union of two Lists

li = [3, 5, 2, 6, 7]
li2 = [98, 6, 54, 23]

li3 = li.copy()

for i in li2:
    if i not in li3:
        li3.append(i)

print("Union of lists:", li3)