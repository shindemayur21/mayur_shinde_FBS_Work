#  WAP to print all even numbers until n.

num = int(input("Enter a number : "))

for i in range(1, num):
    if (i % 2 != 0):
        print(f'{i} is Odd number')

# for i in range(1, num+1, 2): # Used this as we know Odd no are 1, 3, 5, 7 and so on
#     print(f'{i} is Odd number')