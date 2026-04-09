# 13. Python Program to count number of digits and letters in a string.

str = input("Enter any string : ")

dg = 0
ltr = 0
for chr in str:
    if chr.isdigit():
        dg += 1
    elif chr.isalpha():
        ltr += 1

print(f'Count of Digits in string is : {dg}')
print(f'Count of Letters in string is : {ltr}')
