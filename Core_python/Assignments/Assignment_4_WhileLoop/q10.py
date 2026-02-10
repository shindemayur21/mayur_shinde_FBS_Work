# WAP to check if given number is Perfect Number.
# A perfect number is a positive integer that’s equal to the sum of its proper divisors.
# Example
# Take 6:
# Proper divisors: 1, 2, 3
# Sum: 1 + 2 + 3 = 6

n = int(input("Enter a number : "))
temp = n
i = 1
sum = 0
while (i < n):
    if (n % i == 0):
        # print(f'{i} is divisor of {n}')
        sum += i
    i += 1
if(sum == temp):
    print(f'{temp} is a perfect number')
else:
    print(f'{temp} is not a perfect number')