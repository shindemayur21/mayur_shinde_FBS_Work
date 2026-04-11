# Check strong number using function.
def strongNumber(n):

    temp = n
    sum = 0
    while (n > 0):
        d = n % 10
        fact = 1
        for i in range(1, d+1):
            fact = fact * i
        sum = sum + fact
        n = n//10

    if temp == sum:
        return f'{temp} is Strong number'
    else:
        return f'{temp} is not Strong number'

num = int(input("Enter a number : "))
res = strongNumber(num)
print(res)