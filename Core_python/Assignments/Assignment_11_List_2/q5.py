# li = ['desktop', 'users', 'coret', 'pythonoptop', 'shinde']

# Bubble sort based on length
def strSort():
    n = len(li)

    for i in range(n):
        for j in range(0, n - 1):
            if len(li[j]) > len(li[j + 1]):
                # Swap
                li[j], li[j + 1] = li[j + 1], li[j]


li = ['desktop', 'users', 'core', 'pythonoptop', 'shinde']

print('Before swapping : ', li)
strSort()
print('after swapping : ', li)
