#Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount.

amount = int(input("Enter amount : "))

#code for 500 rs. notes
f_hndrd = (amount /500)
print(f'{int(f_hndrd)} notes of 500 will require')

#code for 200 rs. notes
t_hndrd = (amount /200)
print(f'{int(t_hndrd)} notes of 200 will require')

#code for 100 rs. notes
hndrd = (amount /100)
print(f'{int(hndrd)} notes of 100 will require')

#code for 50 rs. notes
fifty = (amount /50)
print(f'{int(fifty)} notes of 50 will require')

#code for 20 rs. notes
twenty = (amount /20)
print(f'{int(twenty)} notes of 20 will require')

#code for 10 rs. notes
tenth = (amount /10)
print(f'{int(tenth)} notes of 10 will require')