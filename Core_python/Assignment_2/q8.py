#Write a program to swap two numbers using third variable.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(f'Number before swapping : {num1} & {num2}')

temp = num1
num1 = num2
num2 = temp

print(f'Number after swapping : {num1} & {num2}')