# 7. Write a program to create a new list from existing list which contains cube of each number of list.

li = [3, 4, 5, 1, 2]

li2 = []

for i in li:
    i = i**3
    li2.append(i)

print("Cube of elements from the list :", li2)
