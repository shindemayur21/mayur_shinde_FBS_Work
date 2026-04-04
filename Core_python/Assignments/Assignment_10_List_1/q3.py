# 3. Write a program to find the second largest element in the list.

li = [23, 65, 24, 10, 81, 42, 2, 9]

max = li[0]
smax = 0

for i in range(1, len(li)):
    if li[i] > max:
        smax = max
        max = li[i]
    elif (li[i] > smax):
        smax = li[i]
print(f'Max element is : {max} and Second max is : {smax}')
    