#Write a program to convert days into years, weeks and days.

dayss = int(input("Enter days count : "))

yrs = dayss / 365
wks = dayss / 7
dys = dayss / 1

print(f'Days converted into Days : {dys:.0f}, Weeks : {wks:.2f}, Years : {yrs:.2f} : ')