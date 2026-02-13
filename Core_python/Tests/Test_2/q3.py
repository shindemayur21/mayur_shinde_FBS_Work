rad = int(input("Enter radius of circle : ")) # radius = 20
l = int(input("Enter length of rectangle : ")) # length = 50
b = int(input("Enter breadth of rectangle : ")) # breadth = 40

hCircle = (0.5 * (2 * 3.14 * rad)) * 35 # fencing for half circle field

hRect = (2*l + b) * 35 # fencing for half rectangle field

totFence = (hCircle + hRect) # fencing of total field

totCost = totFence * 5 # fenching after barbing wire 5 times

print(f'Total cost of fencing the field is : {totCost} Rs.')