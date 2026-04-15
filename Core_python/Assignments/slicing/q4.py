s = "ABCDEFGHIJ"

# 1.Output: ACEGI
print(s[0::2])
print(s[::2])

# 2.Output: JHFDB
print(s[::-2])
print(s[-1::-2])

# 3.Output: EDCBA
print(s[4::-1])
print(s[-6::-1])

# 4.Output: BDFH
print(s[1:-2:2])
print(s[1:8:2])

# 5.Output: IHGFE
print(s[-2:3:-1])
print(s[8:3:-1])
