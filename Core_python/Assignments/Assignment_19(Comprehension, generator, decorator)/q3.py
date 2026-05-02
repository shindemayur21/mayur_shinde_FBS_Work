# 3. Count the number of spaces in a string (take input from user)

text = input("Enter a string: ")

count = sum(1 for char in text if char == ' ')

print("Number of spaces:", count)
