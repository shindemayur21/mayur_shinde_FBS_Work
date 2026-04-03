# 1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +….. + n!


def factorial(n):  # to calculate factorial
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def sum_of_series(n):  # to calculte sum of series
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_of_series(n - 1)


n = int(input("Enter a number: "))

res = sum_of_series(n)
print(f'Sum of series is : {res}')
