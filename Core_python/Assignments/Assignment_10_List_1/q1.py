# 1. Write a program to find sum of all elements of list

li = [30, 40, 501, 10, 20]

sum = 0
for ind in range(0, len(li)):
    sum = sum + li[ind]

print(sum)