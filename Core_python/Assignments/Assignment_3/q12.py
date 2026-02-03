# Write a program to check if given 3 digit number is a palindrome or not.

ogNum = int(input("Enter any 3 digit number : "))

dig1 = (ogNum // 100)
dig2 = ((ogNum // 10) % 10) * 10
dig3 = (ogNum % 10) * 100

revNum = dig3 + dig2 + dig1

if revNum == ogNum:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")