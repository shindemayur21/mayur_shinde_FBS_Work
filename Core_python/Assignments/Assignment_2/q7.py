#Find the sum of three-digit number.

num = int(input("Enter any 3 digit number : "))

sum = (num // 100) + ((num // 10) % 10) + (num % 10)

print(f'Addition of 3 digit number is : {sum}')