# 3. Python Program to Detect if Two Strings are Anagrams

while False:
    str1 = input("Enter first string : ")
    str2 = input("Enter second string : ")

    if len(str1) == len(str2):
        isAnagram = True
        for i in str1:
            if str1.count(i) != str2.count(i):
                isAnagram = False

        if isAnagram:
            print("String is Anagram")
        else:
            print("String is not anagram")
    else:
        print("String is not anagram")
