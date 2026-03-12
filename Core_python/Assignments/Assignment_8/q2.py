# 2. Write a program to calculate area of circle

def circArea(ro):
    return 3.14 * (ro ** 2)
    

r = int(input("Enter radius : "))

print(f'Area of Cirle is {circArea(r)}')