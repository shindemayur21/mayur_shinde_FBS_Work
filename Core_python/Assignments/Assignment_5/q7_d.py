# Write a program to solve the following series :
# d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10  

nSer = int(input("Enter a number for series : "))
a = float(input("Enter value of a : "))

sum = 0
for i in range(1, nSer+1):
    mulDiv = (a * i) / i
sum = sum + mulDiv
print(f'S = a + a2 / 2 + a3 / 3 + …… + aN / N : {sum:.2f}')