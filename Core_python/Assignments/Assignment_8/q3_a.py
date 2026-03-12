# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+….. + n

def add(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

num = int(input("Enter range : "))
print(f'Sum of 1+ 2 + 3 + 4+….. + {num} : {add(num)}')