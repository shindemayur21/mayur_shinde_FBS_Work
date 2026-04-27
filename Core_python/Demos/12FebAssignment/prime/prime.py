# Check prime no or not

n = int(input("Enter a number : "))

for i in range(2, n):
    if (n % i == 0):
        break
else:
    print (f'{n} is prime number')