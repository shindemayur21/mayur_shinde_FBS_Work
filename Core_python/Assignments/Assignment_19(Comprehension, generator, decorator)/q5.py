# 5. Find all of the words in a string that are less than 5 letters (take input from user)

text = input("Enter a string : ")

result = [wd for wd in text.split() if len(wd) < 5]

print("Words less than 5 letters : ", result)
