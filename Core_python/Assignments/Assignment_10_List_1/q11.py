# 11. Write a program to print all numbers which are divisible by m and n in the list.

li = [23, 12, 48, 27, 39, 6, 78]

li2=[]

m = 2
n = 3

for i in li:
    if i % 2 == 0 and i % 3 == 0:
        li2.append(i)

print(f'List of elements divisible by {m} & {n} : {li2}')