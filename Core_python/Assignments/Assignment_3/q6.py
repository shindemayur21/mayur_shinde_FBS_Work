#Write a program to calculate profit or loss.

cp = float(input("Enter cost price :"))
sp = float(input("Enter selling price : "))

if sp > cp:
    print("Profit")
else:
    print("Loss")