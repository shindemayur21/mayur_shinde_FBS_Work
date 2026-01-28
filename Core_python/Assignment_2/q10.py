#Write a program to reverse three-digit number.

num = int(input("Enter any 3 digit number : "))

dig1 = (num // 100)
dig2 = ((num // 10) % 10) * 10
dig3 = (num % 10) * 100

print(f'Reverse no is : {dig3 + dig2 + dig1}')