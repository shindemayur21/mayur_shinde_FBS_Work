m = 1
for i in range(1, 6):
    m = i
    for j in range(1, 5+1):
        if(i==2 and j==2) or (i==2 and j==3) or (i==3 and j==2):
            print(' ',end=' ')
        elif (m <= 5):
            print(m, end=' ')
        m = m + 1
    print()