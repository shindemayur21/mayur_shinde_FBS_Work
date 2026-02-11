# WAP to print Fibonacci series upto n.

num = int(input("Enter a number for Fibonacci series : "))

a = -1
b = 1
i = 1
for i in range(num):
    c = a + b
    print(c)
    a, b = b, c