# 8. Write a program to create a duplicate of an existing list. It should not point to same list.

li = [3, 4, 5, 1, 2]

li2 = []

for i in li:
    li2.append(i)

print("Duplicate of an existing list:", li2)
