# 7. Write a program to find sum of digits of a number.

def sumDig(n):
    sum = 0
    while (n > 0):
        d = n % 10
        sum = sum + d
        n = n // 10
    return sum

num = int(input("Enter range : "))
print(f'Sum of digits of a {num} : {sumDig(num)}')