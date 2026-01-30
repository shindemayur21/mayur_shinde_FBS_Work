#Write a program to calculate area of an equilateral triangle.

a = int(input("Enter Side : "))

#squar root of 3 for equilateral triangle
down_one = int(input("Enter closest lower sqrt no :"))
sqr_d = down_one + (3 - (down_one ** 2)) / (2 * down_one)


eArea = (sqr_d / 4) * (a ** 2)
print(f'Area of equilateral triangle is : {eArea:.2f}')