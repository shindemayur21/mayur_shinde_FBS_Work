for i in range(4):
    num = 1
    print(" " * (4 - i), end="")   # spacing for triangle shape
    
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)  # calculate next value
    print()