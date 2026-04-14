# 3. Write a Python program to find all the unique words and
# count the frequency of occurrence from a given list of strings.
# Use Python set data type.

str = "find all the unique all word"

s1 = str.split(' ')

wrd = set(s1)
wdCnt = set()

for i in wrd:
    cnt = s1.count(i)
    wdCnt.add((i,cnt))

print(wdCnt)
