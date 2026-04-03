# 2. Write a program to check if given number is Armstrong or not using recursive function.

def armstrong_sum(num, pwr):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** pwr) + armstrong_sum(num // 10, pwr)

n = int(input("Enter a number: "))

# Find number of digits
num_digits = len(str(n))

# Calculate sum using recursion
result = armstrong_sum(n, num_digits)

# Check Armstrong condition
if result == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")