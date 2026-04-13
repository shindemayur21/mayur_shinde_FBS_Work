# 5. Python Program to Sum All the Items in a Dictionary

add = {}

n = int(input("Enter a number : "))
sum = 0

#Loop to put elements in dictionary
for i in range(n+1):
    add[i] = i

#loop for get sum of all elements from dictionary
for val in add.values():
    sum = sum + val

print(add)
print(f'Sum is : {sum}')