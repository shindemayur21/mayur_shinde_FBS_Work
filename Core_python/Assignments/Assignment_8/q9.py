# 9. Write a program to check if entered number is a palindrome or not.

def revNum(n):
    temp = n
    sum = 0
    while (n > 0):
        d = n % 10
        sum = (sum * 10) + d
        n = n // 10
    return sum == temp

num = int(input("Enter range : "))

if revNum(num):
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')