for i in range(0, 5):
    for j in range(1, 5 - i):
        print(' ' * int(2), end=' ')  # prints 1 space
        
    for j in range(1, i+2):
        print(j, end=' ')
        print(' ' * int(3), end=' ')
    print()