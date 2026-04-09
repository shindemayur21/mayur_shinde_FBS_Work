# 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

str1 = "Mayur Shinde"

if len(str1) < 2:
    new_str = str1
else:
    new_str = str1[-1] + str1[1:-1] + str1[0]

print("New string after swapping :", new_str)