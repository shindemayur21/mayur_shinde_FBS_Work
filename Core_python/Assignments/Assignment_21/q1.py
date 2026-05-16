# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    opr = input("Enter operator (+, -, *, /): ")

    if opr == '+':
        print(add(num1, num2))

    elif opr == '-':
        print(sub(num1, num2))

    elif opr == '*':
        print(mul(num1, num2))

    elif opr == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        print(div(num1, num2))

    else:
        raise ValueError("Invalid operator")

except ValueError as v:
    print("Invalid input:", v)

except ZeroDivisionError as z:
    print("Math error:", z)

except Exception as e:
    print("Unexpected error:", e)