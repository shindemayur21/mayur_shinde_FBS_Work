# find building cost for Interior & Exterior
# area = l * side, perimeter = 4 * side

sideCost = float(input("Enter cost of painting for one side : "))

aSquare1 = sideCost ** 2
print(f'Cost to paint Interior of building 1 is : {aSquare1}')

PerSquare1 = 4 * sideCost
print(f'Cost to paint Exterior of builing 1 is : {aSquare1}')

aSquare2 = (sideCost * (1/3)) ** 2
print(f'Cost to paint Interior of building 2 is : {aSquare2:.2f}')

PerSquare2 = (4 - 1) * sideCost
print(f'Cost to paint Exterior of builing 2 is : {PerSquare2}')