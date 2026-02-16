# Write a program to solve the following series :
# s = x - x2/3 + x3/5 - x4/7 + …. to n terms

nSer = int(input("Enter a number for series : "))
x = float(input("Enter value of x : "))
sum = 0
for i in range(1, nSer+1):
    tot = ((-1) ** (i - 1)) * (x * i) / (2 * i -1)
sum = sum + tot
print(f'x - x2/3 + x3/5 - x4/7 + ... : {sum:.2f}')