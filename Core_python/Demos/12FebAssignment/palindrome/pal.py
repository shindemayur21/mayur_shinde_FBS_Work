# WAP to check Palindrome number

num = int(input("Enter a number : "))

temp = num
cnt = 0
rev = 0
for _ in str(num):
    cnt += 1

for i in range(cnt, 0, -1):
    d = num %  10
    rev = (rev * 10) + d
    num //= 10

if (temp == rev):
    print(f'{temp} is a palindrome number')