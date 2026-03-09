m = 1
for i in range(0, 5):
    for j in range(1, 5 - i):
        print(' ', end=' ')
    for j in range(1, i+2):
        print(j, end=' ')

    m = 1 * i
    for j in range(1, i+1):
        print(m, end=' ')
        m = m -1
    print()