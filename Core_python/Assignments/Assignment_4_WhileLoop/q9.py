# WAP to print all numbers in a range divisible by a given number.

nRange = int(input("Enter range : "))
n = int(input("Enter a number : "))

i = 1
while (i <= nRange):

    if (i % n == 0):
        print(f'{i} is divisible by {n}')
    i += 1
