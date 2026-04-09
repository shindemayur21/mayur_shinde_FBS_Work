# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String

str = "Mayur Shinde"

wrd = 1
chr = 0
## Method 1
for i in str:
    chr += 1
    if i == ' ':
        wrd += 1

print(f'Number of words : {wrd}')
print(f'Number of Characters : {chr}')

## Method 2
# chr = len(str)
# wrdCnt = len(str.split(' '))

# print(f'Number of words : {wrdCnt}')
# print(f'Number of Characters : {chr}')