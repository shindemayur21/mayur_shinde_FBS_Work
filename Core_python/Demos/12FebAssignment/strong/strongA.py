# WAP to print Strong number within a given range

nRange = int(input("Enter a number for a range : "))

for n in range(1, nRange+1):

    temp = n
    cnt = 0
    sum = 0
    for _ in str(n):
        cnt += 1

    for i in range(cnt, 0, -1):
        d = n % 10
        fact = 1
        for m in range(d, 0, -1):
            fact = fact * m
        sum = sum + fact
        n //= 10

    if(temp == sum):
        print(f'{temp} is a strong number')