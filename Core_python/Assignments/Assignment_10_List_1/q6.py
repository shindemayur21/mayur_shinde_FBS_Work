# 6. Write a program to remove duplicates from the list

li = [23, 65, 2, 10, 817, 425, 2, 9, 65]

li2 = []

for i in li:
    if i not in li2:
        li2.append(i)

print("List after removing duplicates:", li2)