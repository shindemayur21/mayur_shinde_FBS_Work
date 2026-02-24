# WAP to print Perfect number for n range.

nRange = int(input("Enter a number of range : "))

cnt = 0
for n in range(1, nRange):
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            sum += i
        
    if(n == sum):
        print(f'{n} is perfect number')
        cnt += 1
        if (cnt == 3):
            break