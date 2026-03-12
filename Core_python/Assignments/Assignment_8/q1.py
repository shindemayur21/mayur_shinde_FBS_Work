# 1. Write a program to calculate area of rectangle

def rectArea(lo, bo):
    return lo * bo

l = int(input("Enter length : "))
b = int(input("Enter breadth : "))

print(f'Area of rectangle is {rectArea(l,b)}')