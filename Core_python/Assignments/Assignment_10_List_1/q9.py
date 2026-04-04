# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

li = [3, 4, 5, 1, 2, 98, 67, 0, 45, 6]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f'List of even numbers : {even}')
print(f'List of odd numbers : {odd}')
