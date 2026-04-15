s = "PythonProgramming"

# 1.Reverse only "Programming" part
# method1
# pth = s[:6]
# prg = pth + s[-1:5:-1]
# print(prg)

# method2
# result = s[:6] + s[6:][::-1]
# print(result)

# 2.Get "nohtyP" (reverse only first word part)
# print(s[:6][::-1])
# print(s[5::-1])\

# 3.Extract "gram" using slicing
# print(s[-8:-4])
# print(s[9:13])

# 4.Reverse string but skip every 2nd character
# print(s[-1::-2])
# print(s[::-2])
# print(s[len(s)-1::-2])

# 5.Get middle 5 characters
# size = len(s)
# mid = size // 2
# print(s[mid-2:mid+3])
