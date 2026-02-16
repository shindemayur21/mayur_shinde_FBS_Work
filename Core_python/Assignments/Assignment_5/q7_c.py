# Write a program to solve the following series :
# Find the sum of a geometric series from 1 to n where the common ratio is 2.

nSer = int(input("Enter a number for series : "))
sum = 0
for n in range(1, nSer+1):
    geoRatio = (2 ** n) - 1
sum = sum + geoRatio
print(f'sum of a geometric series with common ratio is 2 : {sum}')