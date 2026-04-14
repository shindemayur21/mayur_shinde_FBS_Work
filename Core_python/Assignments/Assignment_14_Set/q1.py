# 1. Write a Python program to find elements in a given set that are not in another set.

s1 = {1, 2, 3, 5, 6}
s2 = {3, 4, 5, 7, 8}

print(s1.difference(s2))  # Method 1
print(s1-s2)  # Method 2
