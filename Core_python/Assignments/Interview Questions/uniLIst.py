# Take two list & create unique list from both list elements

li1 = [5, 30, 7, 2, 12, 9]
li2 = [7, 12, 5, 87, 0, 2]


for i in li2:
    if i in li1:
        pass
    else:
        li1.extend([i])
print(li1)
