s = "Python123"

# 1.Get every 2nd character
print(s[1::2])

# 2.Get every 3rd character
print(s[::3])

# 3.Start from index 1 and take every 2nd character
print(s[1::2])

# 4.Reverse the string using slicing
print(s[len(s)-1: : -1])
print(s[::-1])

# 5.Get characters from index 7 to 2 (reverse order)
print(s[7:1:-1])