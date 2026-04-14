# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

li = ["eat", "tea", "tan", "ate", "nat", "bat"]

s1 = set()

for j in range(0, len(li)-1):
    for i in range(j+1, len(li)-1):
        # print(i, len(i))
        str1 = li[j]
        str2 = li[i]
        if len(str1) == len(str2):
            isAnagram = True
            for ch in str2:
                if str1.count(ch) != str2.count(ch):
                    isAnagram = False
                    break
            if isAnagram:
                s1.add((str1, str2))
print(s1)
