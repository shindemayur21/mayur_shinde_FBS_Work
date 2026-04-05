# 9. Write a program to create three lists of numbers, their squares and cubes.

li = []
sqr = []
cbs = []

n = int(input("How many elements you want to enter in list : "))

for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))

    li.append(ele)

    sq = ele**2
    sqr.append(sq)

    cb = ele**3
    cbs.append(cb)

print("Normal list :", li)
print("Square of list elements : ", sqr)
print("Cube of list elements ", cbs)
