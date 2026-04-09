# 6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

str = "Python Program to Take in a String and Replace Every Blank Space with Hyphen"

# 1. with replace method
# newStr = str.replace(' ','-')
# print(newStr)

# 1. without replace method
newStr = ''
for i in str:
    # print(i)
    if i != ' ':
        newStr = newStr + i
    else:
        newStr = newStr + '-'
print(newStr)
