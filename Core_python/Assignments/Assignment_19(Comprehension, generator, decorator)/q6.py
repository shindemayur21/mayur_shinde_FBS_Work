# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)


text = input("Enter a string : ")

result = {wd: len(wd) for wd in text.split()}

print("Words less than 5 letters : ", result)
