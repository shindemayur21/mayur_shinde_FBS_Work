#  WAP to print all even numbers until n.

num = int(input("Enter a number : "))

for i in range(1, num+1):
    if (i % 2 == 0):
        print(f'{i} is Even number')

# for i in range(0, num+1, 2): # Used this as we know even no are 0, 2, 4, 6 and so on
#     print(f'{i} is Even number')