# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

def bubbleSort():
    size = len(li)

    for i in range(1, size):
        for j in range(0, size - 1):
            if (li[j] > li[j + 1]):
                li[j], li[j+1] = li[j+1], li[j]

def secMax():
    max = li[0]

    for i in range(1, len(li)):
        if li[i] > max:
            smax = max
            max = li[i]
        elif (li[i] > smax):
            smax = li[i]
    return smax

li = [23, 65, 24, 10, 81, 425, 2, 9]
print('Before swapping : ',li)
bubbleSort()
smax = 0
print(secMax())