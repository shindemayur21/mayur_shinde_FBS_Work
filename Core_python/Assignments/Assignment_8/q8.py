# 8. Write a program find reverse of a number

def revNum(n):
    sum = 0
    while (n > 0):
        d = n % 10
        sum = (sum * 10) + d
        n = n // 10
    return sum

num = int(input("Enter range : "))
print(f'Sum of digits of a {num} : {revNum(num)}')