wCost = float(input("Enter cost of single wall : "))

IntCost = wCost ** 2 # Interior of building
print(f'Total cost of buldings interior painting is : {IntCost:.2f} Rs.')

ExtCost = 4 * wCost  # Exterior of building
print(f'Total cost of buldings exterior painting is : {ExtCost:.2f} Rs.')