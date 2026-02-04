# Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

units = int(input("Electricity units : "))

remUnit = units

if remUnit > 50: # first 50 units (0-50)
    remUnit = units - 50
    Amt = (50 + (50 * 0.50))
    totBill = (Amt * 0.2) + Amt #Adding 20% to the bill
    print(f'Amount of first 50 units : {totBill}')
        
    if remUnit > 100: # next 100 units (50-150)
        remUnit = units - 100 # 120
        Amt = (100 + (100 * 0.75))
        totBill += Amt
        totBill = totBill + (totBill * 0.20) #Adding 20% to the bill
        print(f'Amount of (50-150) units : {totBill}')

        if remUnit > 100: # next 100 units (150-250)
            remUnit = units - 100 # 20
            Amt = (100 + (100 * 1.20))
            totBill += Amt
            totBill = totBill + (totBill * 0.20) #Adding 20% to the bill
            print(f'Amount of (150-250) units : {totBill}')

            if remUnit > 100: # next (250 above) units
                remUnit = units - 100 # 20
                Amt = (remUnit + (remUnit * 1.50))
                totBill += Amt
                totBill = totBill + (totBill * 0.20) #Adding 20% to the bill
                print(f'Amount of remaining units : {totBill}')
            else:
                remUnit = units - 100 
                Amt = (remUnit + (remUnit * 1.50))
                totBill += Amt
                totBill = totBill + (totBill * 0.20) #Adding 20% to the bill
                print(f'Amount of remaining units : {totBill}')
else:
    Amt = (remUnit + (remUnit * 0.50)) # if units are less than 50 (0-50)
    totBill = (Amt + (Amt * 0.2)) #Adding 20% to the bill
    print(f'Amount of first 50 units : {totBill}')
