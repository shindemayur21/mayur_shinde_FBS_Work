#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

c_temp = int(input("Enter temperature in Cel : "))

f_temp = ((9/5) * c_temp) + 32

#round() returns a float
print(f'Temperature in Fahrenheit : {round(f_temp,2)}')

#Formatting (f"{x:.2f}") returns a string
print(f'Temperature in Fahrenheit : {f_temp:.2f}')
