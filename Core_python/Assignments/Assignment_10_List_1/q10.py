# 10. Write a program to remove all occurrences of a given element in the list.

li = [3, 4, 5, 1, 2, 98, 67, 2, 45, 6]

li2 = []

ele = int(input("Enter element you want to remove from list : "))

for i in li:
    if i != ele:
        li2.append(i)

print(f'List after removing given element : {li2}')