# WAP to print Palindrome number between given range

sn = int(input("Enter a starting number of range : "))
ln = int(input("Enter a last number of range : "))

for num in range(sn, ln+1):
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