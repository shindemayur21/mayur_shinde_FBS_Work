for i in range(1, 6):
    for j in range(1, 6 - i):
        print(' ', end=' ')

    for j in range(0, i):
        print(chr(65+j), end=' ')

    m = 65 + i
    for j in range(i-1):
        print(chr(m+j), end=' ')
    print()