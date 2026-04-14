# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.


li = [5, 7, 2, 8, 1, 3, 0, 4, 9, 6]
val = int(input("Enter value : "))

size = len(li)
s1 = set()

for i in range(0, size):
    for j in range(i+1, size):
        for k in range(i+2,size):
            if (li[i] + li[j] + li[k]) == val:
                s1.add((li[i], li[j], li[k]))
print(s1)
