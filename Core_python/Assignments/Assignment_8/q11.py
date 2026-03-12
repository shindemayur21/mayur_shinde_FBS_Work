# 11. WAP to check if a given number is Armstrong number or not.
# For each task create separate functions.

def armNum(n):
    temp = n
    sum = 0
    while (n > 0):
        sum = sum + (mod(n) ** 3)
        n = den(n)
    return sum == temp

def mod(r):
    return r % 10

def den(nn):
    return nn // 10

num = int(input("Enter a number : "))

if armNum(num):
    print('Armstrong Number')
else:
    print('Not a Armstrong number')