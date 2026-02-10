# Write a program to check if given number is Armstrong number or not.

num = int(input("Enter a number : "))

cnt = 0
temp = num

while (temp > 0):
    temp = temp // 10
    cnt += 1
print(f'Digits : {cnt}')

temp = num
arm = 0
while(temp > 0):
    r = temp % 10
    arm = arm + (r ** cnt)
    temp = temp // 10

print(f'Arm : {arm}')

if(arm == num):
    print("Armstrong Number")
else:
    print("Not armstrong number")