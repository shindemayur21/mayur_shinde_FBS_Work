# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.

str = "Python Program to Count to the Frequency"

words = str.split(' ')

dict ={}

# print(dict.update(words))

for wd in words:
    if wd in dict:
        dict[wd] += 1
    else:
        dict[wd] = 1

# Display result
print("Word Frequency:", dict)