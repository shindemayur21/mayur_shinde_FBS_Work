# check leap or not

yr = int(input("Enter a year : "))

if (yr % 4 == 0):      # if year is divisible by 4
    if (yr % 100 == 0):     # if year is divisible by 100
        if (yr % 400 == 0):     # if year is divisible by 400
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
