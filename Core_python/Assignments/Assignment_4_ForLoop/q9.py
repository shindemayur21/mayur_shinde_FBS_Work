# WAP to print all numbers in a range divisible by a given number.

nRange = int(input("Enter range : "))
n = int(input("Enter a number : "))

for i in range(1, nRange+1):

    if (i % n == 0):
        print(f'{i} is divisible by {n}')