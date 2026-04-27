# print prime nos Between range
sn = int(input("Enter starting number of range : "))
ln = int(input("Enter last number of range : "))

for num in range(sn, ln+1):
    for i in range(2, num):
        if (num % i == 0):
            break
    else:
        if (num >= sn and num <= ln):
            print(f'Prime no : {num}')
