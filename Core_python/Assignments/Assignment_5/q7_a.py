# Write a program to solve the following series :  
# a. 1! + 2! + 3! + 4! + …..n!  


nSer = int(input("Enter a number for series : "))
sum = 0
for num in range(1, nSer+1):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    sum = sum + fact
print(f'1! + 2! + 3! + 4! + …..n! : {sum}')