# 6. Python Program to Multiply All the Items in a Dictionary.

di = {}

n = int(input("Enter a number : "))

for i in range(1, n+1):
    di[i] = i

print(di)

mult = 1
for val in di.values():
    mult = mult * val

print(f'Multiplication of all items in dictionary is : {mult}')
