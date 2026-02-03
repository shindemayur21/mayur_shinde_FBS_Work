# Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input("Enter side1 (must be > 0): "))
side2 = int(input("Enter side2 (must be > 0): "))
side3 = int(input("Enter side3 (must be > 0): "))

if ((side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2)):
    print("Valid triangle")
else:
    print("Invalid triangle")
