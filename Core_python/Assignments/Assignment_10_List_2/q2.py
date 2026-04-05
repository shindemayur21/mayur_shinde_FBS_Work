# 2. Python Program to Merge Two Lists and Sort it

li = [13, 5, 2, 26, 7]
li2 = [98, 23, 54, 23]

li3 = li + li2

print(f'List before sorting : {li3}')
# Loop through list
for i in range(0, len(li3)):
    for j in range(0, len(li3) - 1):
        if li3[j] > li3[j + 1]:
            # Swap
            li3[j], li3[j + 1] = li3[j + 1], li3[j]

print(f'List after sorting : {li3}')