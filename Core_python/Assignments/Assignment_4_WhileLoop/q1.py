#  WAP to print all even numbers until n.

num = int(input("Enter a number : "))

i = 0

while (i <= num):
    if (i % 2 == 0):
        print(f'{i} is Even number')
    i += 1