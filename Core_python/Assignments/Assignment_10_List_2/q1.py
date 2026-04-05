# 1. Python Program to Put Even and Odd elements of a List into two Different Lists

li = [3, 4, 5, 1, 2, 98, 67, 0, 45, 6]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f'List of even numbers : {even}')
print(f'List of odd numbers : {odd}')
