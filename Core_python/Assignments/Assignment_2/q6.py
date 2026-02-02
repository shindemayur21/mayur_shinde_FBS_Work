#WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

#Enter Baic salary
bas_sal = float(input("Enter basic salry : "))

da = bas_sal * (10/100)
ta = bas_sal * (12/100)
hra = bas_sal * (15/100)

#formula to calculate total salary
tot_sal = bas_sal + da + ta + hra

#Print total salary
print(f'Total salary is : {tot_sal} Rs.')