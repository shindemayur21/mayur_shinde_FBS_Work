# Factorial of number

num = int(input("Enter a number : "))
fact = 1
while (num > 1):
    print(fact)
    fact *= num
    num -= 1
print(fact)
print(f'factorial numbers is : {fact}')