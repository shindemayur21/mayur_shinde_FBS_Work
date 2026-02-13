prod1 = float(input("Enter price of product 1 : "))
prod2 = float(input("Enter price of product 2 : "))
prod3 = float(input("Enter price of product 3 : "))
prod4 = float(input("Enter price of product 4 : "))
prod5 = float(input("Enter price of product 5 : "))

Tot = prod1 + prod2 + prod3 + prod4 + prod5   # products total

gstTot = Tot + (Tot * 0.18)      # Final total after GST

print(f'Total bill after 18% GST : {gstTot} Rs.')