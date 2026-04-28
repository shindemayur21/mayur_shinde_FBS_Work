# Snake Ladder board without list comprehension


li2 = []
for i in range(0, 10):

    li = []
    if i % 2 != 0:
        for ele in range((i + 1) * 10, i * 10, -1):
            li.append(ele)
    elif i % 2 == 0:
        for ele in range(i * 10 + 1, (i + 1) * 10 + 1):
            li.append(ele)

    li2.append(li)
for ele in li2:
       print(ele)
