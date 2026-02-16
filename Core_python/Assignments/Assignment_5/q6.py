# Write a program to print prime numbers between 1 to 100.

n = int(input("Enter a number for range : "))

for i in range(2, n+1):

    temp = True
    j = 2
    while (j >= 2) and (j <= i//2):
        if (i % j == 0):
            temp = False
        j += 1
    if(temp):
        print(f'{i} is a prime number')