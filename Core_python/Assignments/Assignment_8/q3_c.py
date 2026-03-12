# 3. Write a program to find sum of following series using functions :
# c. 1^1 + 2^2 + 3^3+ …… n^n

def addExpo(n):
    sum = 0
    Expo = 0
    for i in range(1, n+1):
        Expo = i ** i
        sum = sum + Expo
    return sum

num = int(input("Enter range : "))
print(f'Sum of 1!+ 2! + 3! + 4!+….. + {num}! : {addExpo(num)}')