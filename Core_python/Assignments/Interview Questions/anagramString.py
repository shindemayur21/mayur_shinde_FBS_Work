str1 = "listan"
str2 = "silent"

if len(str1) == len(str2):
    is_anagram = True
    
    for i in str1:
        if str1.count(i) != str2.count(i):
            is_anagram = False
            break
    
    if is_anagram:
        print("Anagram String")
    else:
        print("Not an Anagram String")
else:
    print("Not an Anagram String")