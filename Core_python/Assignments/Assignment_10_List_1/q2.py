# 2. Write a program to find maximum and minimum element in a list.

li = [30, 40, 501, 10, 20]

max = li[0]
min = li[0]

for i in range(1, len(li)-1):
    if li[i] > max:
        max = li[i]
    elif li[i] < min:
        min = li[i]

print(f'Max element from list is : {max}')
print(f'Min element from list is : {min}')
