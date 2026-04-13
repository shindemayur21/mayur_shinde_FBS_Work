# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not.

di = {id:101,'name':'mayur'}

key = input("Enter the key to check: ") #taking input from user

# Checking if key exists
if key in di:
    print("Key exist in dictionary.")
else:
    print("Key does not exist in dictionary.")