# Write a program to input angles of a triangle and check whether triangle is valid or not.
ang1 = int(input("Enter first angle (should be between 1-90) : "))

if ang1 == 90:
    ang2 = int(input("Enter second angle (should be less than 90) : "))
else:
    ang2 = int(input("Enter second angle (should be between 1-90) : "))

if ang1 == 90 or ang2 == 90:
    ang3 = int(input("Enter third angle (should be less than 90) : "))
else:
    ang3 = int(input("Enter third angle (should be between 1-90) : "))

sum = ang1 + ang2 + ang3

if sum == 180:
    print('Valid triangle')
else:
    print('Invalid triangle')
