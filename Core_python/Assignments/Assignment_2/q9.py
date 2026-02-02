#Write a program to swap two numbers without using third variable

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(f'Number before swapping : {num1} & {num2}')

num1 = num1 + num2 # 2 + 5 = 7
num2 = num1 - num2 # 7 - 5 = 2
num1 = num1 - num2 # 7 - 2 = 5

print(f'Number after swapping : {num1} & {num2}')