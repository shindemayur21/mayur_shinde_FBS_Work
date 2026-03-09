k = 7
m = 1
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    for j in range(1, k+1):
        print(' ', end=' ')
    k -= 2

    m = 1 * i
    if(i==5):
        m = 1 * (i - 1)
    for j in range(1, i + 1):
        if (j == 5):
            break
        else:
            print(m, end=' ')
        m = m - 1
    print()