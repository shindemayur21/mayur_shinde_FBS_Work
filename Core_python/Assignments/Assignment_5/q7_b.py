# Write a program to solve the following series :  
# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)

nSer = int(input("Enter a number for series : "))
n = float(input("Enter value of N : "))
sum = 0
for i in range(1, nSer+1):
    expo = n ** i
sum = sum + expo
print(f'N + N^2 + N^3+N^4 …..+N^N : {sum:.2f}')