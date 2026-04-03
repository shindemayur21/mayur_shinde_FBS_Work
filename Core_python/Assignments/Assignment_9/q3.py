# 3. Write a program to reverse a given number using recursive function.

def revNumber(n, rev=0):
    if n == 0:
        return rev
    return revNumber(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))

# To handle negative numbers
if num < 0:
    reversed_num = -revNumber(-num)
else:
    reversed_num = revNumber(num)

print(f'Reversed number is : {reversed_num}')