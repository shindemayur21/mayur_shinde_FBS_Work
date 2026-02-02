#Write a program to enter P, T, R and calculate simple Interest.

p = float(input("Enter Prnciple : "))
t = float(input("Enter Tenure : "))
r = float(input("Enter ROI : "))

sInt = (p * t * r) / 100

print(f'Simple Interest is : {sInt:.2f}')