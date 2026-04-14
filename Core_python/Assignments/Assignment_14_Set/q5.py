# 5. Write a Python program to find the longest common prefix of all strings.
# Use the Python set

str = "flower flow flight"

wrd = str.split()
s1 = set()
li = []

for w in wrd:
    addChar = ''
    cnt = 0
    for chr in w:
        addChar = addChar + chr
        li.append(addChar)


max = 0
size = 0
longPref = ''
for i in range(len(li)):
    if li.count(li[i]) >= max and len(li[i]) >= size:
        max = li.count(li[i])
        size = len(li[i])
        longPref = li[i]
print(f'"{longPref}" has longest common prefix of "{size}" with "{max}" occurences')
