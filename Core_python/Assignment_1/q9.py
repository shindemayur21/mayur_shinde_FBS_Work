#Write a program to enter base and height of a triangle and find its area

b = int(input("Enter base of triangle : "))
h = int(input("Enter height of triangle : "))

tArea = 1 / 2 * (b * h)

print(f'Area of triangle is : {tArea:.2f}')