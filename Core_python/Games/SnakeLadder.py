# Snake Ladder board with list comprehension


li = [[ele for ele in range(i * 10 + 1, (i + 1) * 10 + 1) if i % 2 == 0] or
       [ele for ele in range((i + 1) * 10, i * 10, -1) if i % 2 != 0]
       for i in range(0, 10)]

for row in li:
    print("+----" * 10 + "+")
    for num in row:
        print(f"|{num:3} ", end="")
    print("|")
print("+----" * 10 + "+")
