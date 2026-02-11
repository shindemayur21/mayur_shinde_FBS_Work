# WAP to check if given number is Perfect Number.
# A perfect number is a positive integer that’s equal to the sum of its proper divisors.
# Example
# Take 6:
# Proper divisors: 1, 2, 3
# Sum: 1 + 2 + 3 = 6

n = int(input("Enter a number : "))
sum = 0
for i in range (1, n):
    if (n % i == 0):
        sum += i

if(n == sum):
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')