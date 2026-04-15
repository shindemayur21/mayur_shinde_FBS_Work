s = "MayurShinde"

# 1.Get last 5 characters
print(s[len(s)-5::])
print(s[-5::])

# 2.Get all except last 2 characters
print(s[:-2:])
print(s[:-2])

# 3.Extract "Shinde" using negative indexing
print(s[5::])
print(s[-6::])

# 4.Extract "yurSh"
print(s[2:-4:])
print(s[-9:-4])

# 5.Remove first and last character
print(s[1:len(s)-1:])
print(s[1:-1])
