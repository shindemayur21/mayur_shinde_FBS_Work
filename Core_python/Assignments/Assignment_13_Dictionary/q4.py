# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

sqr = {}

n = int(input("Enter a number : "))

for i in range(n+1):
    sqr[i] = f'{i} * {i}'

print(sqr)
