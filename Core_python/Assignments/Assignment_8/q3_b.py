# 3. Write a program to find sum of following series using functions :
# b. 1!+ 2! + 3! + 4!+….. + n!

def addFact(n):
    sum = 0
    for i in range(1, n+1):
        fact = 1
        for m in range(1, i+1):
            fact = fact * m
        sum = sum + fact
    return sum

num = int(input("Enter range : "))
print(f'Sum of 1!+ 2! + 3! + 4!+….. + {num}! : {addFact(num)}')