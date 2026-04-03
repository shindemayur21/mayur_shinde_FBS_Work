# 9. Write a program to calculate the m to the power n using recursion.

def pwr(m, n):
    if n == 0:
        return 1
    return m * pwr(m, n - 1)


m = int(input("Enter base : "))
n = int(input("Enter exponent : "))

res = pwr(m, n)
print(f'{m} raised to the power of {n} is : {res}')
