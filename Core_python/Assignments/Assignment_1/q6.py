#Write a Program to input two angles from user and find third angle of the triangle

ang1 = int(input("Enter angle one : "))
ang2 = int(input("Enter angle two : "))

ang3 = 180 - (ang1 + ang2)

print(f' Third angle of triangle is : {ang3}')