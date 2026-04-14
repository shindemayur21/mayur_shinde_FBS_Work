# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers.
# Use the Python set.

li = [5, 7, 21, 8, 10, 3, 0, 4, 9, 6]

size = len(li)
s1 = set()

max = li[0] * li[1]
pair = (li[0], li[1])

for i in range(0, size):
    for j in range(i+1, size):
        if (li[i] * li[j]) > max:
            max = (li[i] * li[j])
            pair = (li[i], li[j])
s1.add((pair, max))
print(s1)
