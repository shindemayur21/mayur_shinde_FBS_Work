# 10. Write a program to check if entered year is a leap year or not.

def leapYear(yr):

    if (yr % 4 == 0) or (yr % 400 == 0):
        print('Leap year')
    elif (yr >= 400) and (yr % 100 == 0):
        print('leap year')
    else:
        print('Not leap year')


num = int(input("Enter a year : "))
leapYear(num)