# WAP to check Armstrong number.

n = int(input("Enter a number : "))

cnt = 0
for _ in str(n):
    cnt += 1

j = n
arm = 0

for m in range(cnt, 0, -1):
    d = n % 10 # 3, 5, 1
    arm = arm + (d ** cnt)
    n = n // 10
    
if(arm == j):
    print(f'{arm} is an Armstrong number')