# WAP to print Fibonacci series upto n.

num = int(input("Enter a number for Fibonacci series : "))

a = 0
b = 1
i = 1
while(i <= num):
    print(a)
    c = a + b
    a,b = b,c
    i += 1