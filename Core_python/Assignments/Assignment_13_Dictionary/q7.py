# 7. Python Program to Remove the Given Key from a Dictionary.

dict = {"a": 2, "b": 3, "c": 4}

print(f'Before removal of key : {dict}')

key = input("Enter a key to remove from dictionary : ")
res = dict.pop(key)

print(f'After removal of key : {dict}')
