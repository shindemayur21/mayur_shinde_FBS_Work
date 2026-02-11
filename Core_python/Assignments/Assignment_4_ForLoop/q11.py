# WAP to check if given number Strong Number.
# A strong number (also called a factorial number) is a number whose sum of the factorials of its digits equals the number itself.
# Take each digit → find its factorial → add them up.
# Example -
# 145 : 1!=1 + 4!=24 + 5!=120
# Sum: 1+24+120=145

num = int(input("Enter a number : "))
sum = 0
cnt = 0
temp = num

for _ in str(temp):
    cnt += 1

for i in range(cnt, 0, -1):
    d = num % 10
    fact = 1

    for j in range(1, d+1):
        fact *= j
    sum += fact
    num = num // 10

if(temp == sum):
    print(f'{temp} is a strong number')
else:
    print(f'{temp} is not a strong number')