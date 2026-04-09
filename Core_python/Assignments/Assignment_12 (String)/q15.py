# 15. Python Program to find larger string without using built-in functions.

str = "Python Program to findgfgfdgfd larger stringssss without using built-in functions"

str2 = str.split(' ')

size = len(str2[0])
lrgWord = str2[0]

for i in str2:
    if len(i) > size:
        size = len(i)
        lrgWord = i
print(f'Larger word from string is : {lrgWord}')
