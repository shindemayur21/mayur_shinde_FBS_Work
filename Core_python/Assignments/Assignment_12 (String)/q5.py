# 5. Python Program to Count the Number of Vowels in a String

str1 = "Python ProgrAm to COunt the NumbEr of Vowels In a String"

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
cnt = 0
for i in str1:
    if i in vowel:
        cnt += 1
print(f'Vowels present in string are : {cnt}')
