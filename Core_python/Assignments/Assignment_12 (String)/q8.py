# 8. Python Program to Remove the Characters of Odd Index Values in a String

str = "Python Program to Remove the Characters of Odd Index Values in a String"

newStr = ''

##1. Method
# cnt = 0
# for i in str:
#     cnt += 1
#     if cnt % 2 != 0:
#         newStr = newStr + i

# print(f'Original String : {str}')
# print(f'New String : {newStr}')


##2. Method
for i in range(len(str)):
    if i % 2 == 0:
        newStr = newStr + str[i]

print(f'Original String : {str}')
print(f'New String : {newStr}')