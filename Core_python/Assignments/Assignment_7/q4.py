k = 1
m = 1
for i in range(0, 5):
    for j in range(1, 5 - i):
        print(' ', end=' ')
        
    for j in range(1, i+2):
        print(k, end=' ')
        k += 1
    k = i +2

    m = 2 * i
    for j in range(1, i+1):
        print(m, end=' ')
        m = m -1

    print()