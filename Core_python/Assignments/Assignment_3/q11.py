# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

p1 = int(input("Enter age of Person1 : "))
amt1 = float(input("Ticket price of Person1 : "))

p2 = int(input("Enter age of Person2 : "))
amt2 = float(input("Ticket price of Person2 : "))

p3 = int(input("Enter age of Person3 : "))
amt3 = float(input("Ticket price of Person3 : "))

p4 = int(input("Enter age of Person4 : "))
amt4 = float(input("Ticket price of Person4 : "))

p5 = int(input("Enter age of Person5 : "))
amt5 = float(input("Ticket price of Person5 : "))

#Calculation for person1
if p1 <= 12:
    tkt1 = amt1 * (30 / 100)
elif p1 >= 60:
    tkt1 = amt1 * (50 / 100)
else:
    tkt1 = amt1

#Calculation for person2
if p2 <= 12:
    tkt2 = amt2 * (30 / 100)
elif p1 >= 60:
    tkt2 = amt2 * (50 / 100)
else:
    tkt2 = amt2

#Calculation for person3
if p3 <= 12:
    tkt3 = amt3 * (30 / 100)
elif p1 >= 60:
    tkt3 = amt3 * (50 / 100)
else:
    tkt3 = amt3

#Calculation for person4
if p4 <= 12:
    tkt4 = amt4 * (30 / 100)
elif p4 >= 60:
    tkt4 = amt4 * (50 / 100)
else:
    tkt4 = amt4

#Calculation for person5
if p5 <= 12:
    tkt5 = amt5 * (30 / 100)
elif p5 >= 60:
    tkt5 = amt5 * (50 / 100)
else:
    tkt5 = amt5

tot = tkt1 + tkt2 + tkt3 + tkt4 + tkt5

print(f'Total Amount of five persons Ticket is {tot:.2f} Rs.')