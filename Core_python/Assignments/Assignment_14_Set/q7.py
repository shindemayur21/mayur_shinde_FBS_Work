# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

s1 = {1, 2, 3, 5, 6}
s2 = {3, 4, 5, 7, 8}

print(s1.symmetric_difference(s2))  # Method 1


# Method 3
s3 = set()

for i in s1:
    if i not in s2:
        s3.add(('s1', i))
for j in s2:
    if j not in s1:
        s3.add(('s2', j))

print(s3)
