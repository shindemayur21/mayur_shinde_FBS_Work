# Write a program to print prime numbers between 1 to 100.

for i in range(1, 100 + 1):

    temp = True
    j = 2

    if(i == 1): # Bcoz prime number starts from 2
        continue

    while (j >= 2) and (j <= i//2):
        if (i % j == 0):
            temp = False
        j += 1
    if(temp):
        print(f'{i} is a prime number')