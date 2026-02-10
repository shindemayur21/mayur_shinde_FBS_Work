# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

n = int(input("Enter a number : "))

i = 1
while (i <= n):
    if (i % 7 == 0 and i % 5 == 0):
        print(f'{i} is divisible by 7 and multiple of 5')
    if (i % 7 == 0):
        print(f'{i} is divisible by 7')
    if (i % 5 == 0):
        print(f'{i} is multiple of 5')
    i += 1