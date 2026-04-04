# 13 . Write a program to print list after removing even numbers.

li = [3, 4, 5, 1, 2, 98, 67, 0, 45, 6]

odd = []

for i in li:
    if i % 2 != 0:
        odd.append(i)

print(f'List of odd numbers : {odd}')
