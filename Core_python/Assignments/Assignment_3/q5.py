# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

ang1 = int(input("Enter first angle (should be between 1-90) : "))

if ang1 == 90:
    ang2 = int(input("Enter second angle (should be less than 90) : "))
else:
    ang2 = int(input("Enter second angle (should be between 1-90) : "))

if ang1 == 90 or ang2 == 90:
    ang3 = int(input("Enter third angle (should be less than 90) : "))
else:
    ang3 = int(input("Enter third angle (should be between 1-90) : "))

side1 = int(input("Enter side1 of triangle : "))
side2 = int(input("Enter side2 of triangle : "))
side3 = int(input("Enter side3 of triangle : "))

if ((side1 == side2 == side3) and (ang1 == ang2 == ang3)):
    print("This is Equilateral triangle")
elif ((side1 == side2 != side3 or side2 == side3 != side1 or side1 == side3 != side2) and (ang1 == ang2 != ang3 or ang2 == ang3 != ang1 or ang1 == ang3 != ang2)):
    print("This is Isosceles triangle")
elif ((side1 != side2 != side3) and (ang1 != ang2 != ang3)):
    print("This is Scalene triangle")
else:
    print("Invalid side or angle measurements")