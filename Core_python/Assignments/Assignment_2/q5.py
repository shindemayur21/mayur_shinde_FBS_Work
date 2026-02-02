#WAP to calculate selling price of book based on cost price and discount.

cp = float(input("Enter cost price : "))
disc = int(input("Enter discount : "))

#calculating selling price after discount
sp = cp - (cp * (disc/100))

print(f'Selling price after {disc}% discount is : {sp}')