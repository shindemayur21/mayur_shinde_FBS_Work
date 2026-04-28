# Snake Ladder board with list comprehension


li3 = [[ele for ele in range(i * 10 + 1, (i + 1) * 10 + 1) if i % 2 == 0] or
       [ele for ele in range((i + 1) * 10, i * 10, -1) if i % 2 != 0]
       for i in range(0, 10)]

for ele in li3:
    print(ele)
