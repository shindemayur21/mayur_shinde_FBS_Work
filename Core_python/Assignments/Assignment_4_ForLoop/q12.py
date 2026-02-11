# Write a program to check if given number is Armstrong number or not.

num = int(input("Enter a number : "))

cnt = 0
temp = num

for d in str(temp):
    cnt += 1

temp = num
arm = 0

for _ in range(cnt, 0, -1):
    r = temp % 10
    arm = arm + (r ** cnt)
    temp = temp // 10

print(f'Arm : {arm}')

if(arm == num):
    print("Armstrong Number")
else:
    print("Not armstrong number")