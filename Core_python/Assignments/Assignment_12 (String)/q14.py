# 14. Python Program to count the occurrences of each word in a string.

str = "python program for for For python developers"

str2 = str.split(' ')

temp = []

for i in range(len(str2)):
    cnt = 0
    if str2[i] not in temp:
        for wrd in str2:

            if str2[i] == wrd:
                cnt += 1

        temp.append(str2[i])
        print(f'{str2[i]} occured {cnt} in string')
