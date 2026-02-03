# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter gender (M/F) : ")
age = int(input("Enter age : "))

if gender in ['F', 'f', 'Female', 'female', 'FEMALE']:
    if age >= 18:
        print("Eligible for marrige")
    else:
        print("Not eligible")
elif gender in ['M', 'm', 'Male', 'male', 'MALE']:
    if age >= 21:
        print("Eligible for marrige")
    else:
        print("Not eligible")