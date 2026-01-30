#Program to Find the Roots of a Quadratic Equation

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

#Discriminant
d = (b * b) - (4 * a * c)
print(d)

#squar root of d
down_one = int(input("Enter closest lower sqrt no :"))
sqr_d = down_one + (d - (down_one ** 2)) / (2 * down_one)

#Printing Discriminant after sqaure root
print(f'Discriminant : {sqr_d}')


root1 = (-b - sqr_d) / (2 * a)
print(f'Roote one value is : {root1}')

root2 = (-b + sqr_d) / (2 * a)
print(f'Roote one value is : {root2}')