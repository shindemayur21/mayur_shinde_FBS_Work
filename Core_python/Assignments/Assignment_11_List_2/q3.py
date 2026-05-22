# 3. Python Program to Sort the List According to the Second Element in Sublist

def Sort(st):
    size = len(li)

    for i in range(1, size):
        for j in range(0, size - 1):
            if (li[j] > st):
                li[j], li[j+1] = li[j+1], li[j]


li = [23, 65, 24, 10, 81, 425, 2, 9]
print('Before swapping : ', li)

li2 = [11, 45, 24, 83, 79]
st = li2[1]

res = Sort(st)
print(li)
