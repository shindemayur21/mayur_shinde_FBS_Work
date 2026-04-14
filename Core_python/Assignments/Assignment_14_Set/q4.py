# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

li = [5, 7, 2, 8, 1, 3, 0, 4, 9, 6]
val = int(input("Enter value : "))

size = len(li)
s1 = set()

for i in range(0, size):
    for j in range(i+1, size):
        if (li[i] + li[j]) == val:
            s1.add((li[i], li[j]))
print(s1)
