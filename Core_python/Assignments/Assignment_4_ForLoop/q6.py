#  WAP to check if a given number is prime number or not.

# Check whether a number is prime using a while loop.

num = int(input("Enter a number : "))
temp = True

for i in range(2, (num // 2) + 1):
    if (num % i == 0):
        temp = False

if (temp):
    print("Prime Number")
else:
    print("Not a prime number")
