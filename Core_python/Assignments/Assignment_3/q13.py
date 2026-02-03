# Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

uCharges = int(input("Electricity charges per unit : "))
units = int(input("Electricity units : "))

amt = uCharges * units

if units <= 50:
    totAmt = (amt + (amt * 0.50))
    totBill = (totAmt + (totAmt * 0.2)) #Adding 20% to the bill
    print(f'Total bill amount is {totBill} Rs.')
    
elif units > 50 and units <= 150:
    totAmt = (amt + (amt * 0.75))
    totBill = (totAmt + (totAmt * 0.2)) #Adding 20% to the bill
    print(f'Total bill amount is {totBill} Rs.')

elif units > 150 and units <= 250:
    totAmt = (amt + (amt * 1.20))
    totBill = (totAmt + (totAmt * 0.2)) #Adding 20% to the bill
    print(f'Total bill amount is {totBill} Rs.')

elif units > 250:
    totAmt = (amt + (amt * 1.50))
    totBill = (totAmt + (totAmt * 0.2)) #Adding 20% to the bill
    print(f'Total bill amount is {totBill} Rs.')