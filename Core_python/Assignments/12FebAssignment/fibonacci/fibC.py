# WAP to print Fibonacci series between range.

sn = int(input("Enter starting number of range : "))
ln = int(input("Enter last number of range : "))

a = -1
b = 1
i = 1

for i in range(ln):
    c = a + b
    if (c >= sn and c <= ln):
        print(c, end=' ')
    a, b = b, c