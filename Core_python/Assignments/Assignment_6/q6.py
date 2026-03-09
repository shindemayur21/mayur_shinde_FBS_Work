k = 3
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(' ', end=' ')

    for j in range(0, i):
        print(j+1, end=' ')

    for j in range(3, i+2):
        print(k, end=' ')
        k += 1
    k = i +2
    print()