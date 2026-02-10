#  WAP to check if a given number is prime number or not.

# Check whether a number is prime using a while loop.

num = int(input("Enter a number : "))
temp = True
i = 2
while(i >= 2) and (i <= num //2):
    if(num % i == 0):
        temp = False
    i += 1

if (temp):
    print("Prime Number")
else:
    print("Not a prime number")