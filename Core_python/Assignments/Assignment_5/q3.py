# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n = int(input("Enter no of passengers : "))
tCost = float(input("Enete tickekt cost : "))
tot = 0
for i in range(1, n+1):
    tPrice = 0
    age = int(input(f'Enter age of {i} passenger : '))
    if (age <= 12):
        tPrice = tCost - (tCost * 0.3) # 30% discount
    elif (age > 59):
        tPrice = tCost - (tCost * 0.5) # 30% discount
    else:
        tPrice = tCost
    print(f'Ticket cost for passenger {i} is : {tPrice:.2f} Rs.')

    tot += tPrice
print(f'Total ticket cost of all passengers is : {tot:.2f} Rs.')