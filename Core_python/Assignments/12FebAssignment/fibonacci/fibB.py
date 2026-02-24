# WAP to print Fibonacci series first n.

num = int(input("Enter a number for Fibonacci series : "))

a = -1
b = 1
i = 1
cnt = 0
for i in range(num):
    c = a + b
    print(c, end=' ')
    a, b = b, c
    cnt += 1
    if cnt == 4:
        break