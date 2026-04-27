# WAP to print Perfect number between given range

sn = int(input("Enter a starting number of range : "))
ln = int(input("Enter a last number of range : "))

for n in range(sn, ln):
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            sum += i
        
    if(n == sum):
            print(f'{n} is perfect number')