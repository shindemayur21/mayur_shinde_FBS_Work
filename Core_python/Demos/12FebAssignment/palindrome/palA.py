# WAP to print Palindrome number within a given range

n = int(input("Enter a number of range : "))

for num in range(n):
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
        print(temp)