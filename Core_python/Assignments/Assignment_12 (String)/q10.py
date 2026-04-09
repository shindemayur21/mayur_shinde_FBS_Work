# 10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

str1 = "Library Function"

strcnt1 = 0
for i in str1:
    strcnt1 += 1

str2 = "Library Func"

strcnt2 = 0
for i in str2:
    strcnt2 += 1

if strcnt1 > strcnt2:
    print(f'String 1 is larger : {str1}')
elif strcnt1 < strcnt2:
    print(f'String 2 is larger : {str2}')
else:
    print("Both string are having equal length")