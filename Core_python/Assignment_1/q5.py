#Write a program to enter P, T, R and calculate simple Interest.

p = float(input("Enter Prnciple : "))
t = float(input("Enter Tenure : "))
r = float(input("Enter ROI : "))

amt = p * (1 + (r/100)) ** t

print(f'Amount is : {amt}')

cInt = amt - p

print(f'Compount Interest is : {cInt:.2f}')