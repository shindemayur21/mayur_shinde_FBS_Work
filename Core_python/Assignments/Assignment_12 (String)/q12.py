# 12. Python Program to count number of lowercase characters in a string.

str = input("Enter any string : ")

cnt = 0
for chr in str:
    if chr.islower():
        cnt += 1

print(f'Count of lowercase in string is : {cnt}')