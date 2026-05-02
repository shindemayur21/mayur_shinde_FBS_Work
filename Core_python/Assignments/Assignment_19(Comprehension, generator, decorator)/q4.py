# 4. Remove all of the vowels in a string (take input from user)

text = input("Enter a string: ")

result = "".join([char for char in text if char.lower() not in "aeiou"])

print("String without vowels:", result)