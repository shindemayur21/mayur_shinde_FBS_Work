#Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter Distance in feel : "))
inches = int(input("Enter Distance in Inches : "))

# formula to convert into meter
mtr = (feet * 0.3048) + ( inches * 0.0254)

#To convert into centimeter
cm = mtr * 100

print(f'Distance in Meter : {mtr} & Centimeter : {cm}.')