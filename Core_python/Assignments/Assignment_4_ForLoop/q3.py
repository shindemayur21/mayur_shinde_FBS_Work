# WAP to print sum of series upto n.

num = int(input("Enter a number : "))

sum = 0
for i in range(1, num+1):
    sum += i

print(f'Total sum of series upto {num} : {sum}')