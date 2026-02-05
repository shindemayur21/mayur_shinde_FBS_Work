# WAP to find area & perimeter of following figure

# Area = ((3/4) * l * b) + ((1/2) * 3.14 * (r ** 2))

l = int(input("Enter Length : "))
b = int(input("Enter breadth : "))
r = int(input("Enter radius : "))

fArea = ((3/4) * l * b) + ((1/2) * 3.14 * (r ** 2))
print(f'Area of figure is : {fArea}')

fPerimeter = (2 * l + b) + ((1 / 2) * 3.14 * r)
print(f'Perimeter of figure is : {fPerimeter}')