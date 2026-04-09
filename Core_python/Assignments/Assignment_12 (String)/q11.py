# 11. Python Program to replace every blank space with hyphen in a string.

str = input("Enter any string : ")

newStr = ''
for i in str:
    # print(i)
    if i != ' ':
        newStr = newStr + i
    else:
        newStr = newStr + '-'
print(newStr)
