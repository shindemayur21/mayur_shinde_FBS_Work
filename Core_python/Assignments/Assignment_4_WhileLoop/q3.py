# WAP to print sum of series upto n.

num = int(input("Enter a number : "))

i = 1
sum = 0
while (i <= num):
    sum += i
    i += 1

print(f'Total sum of series upto {num} : {sum}')