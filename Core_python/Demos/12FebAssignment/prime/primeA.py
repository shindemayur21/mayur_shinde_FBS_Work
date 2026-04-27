# print prime nos till n series

n = int(input("Enter a number for range : "))

for num in range(2, n+1):
    for i in range(2, num):
        if (num % i == 0):
            break
    else:
        print (f'Prime no : {num}')