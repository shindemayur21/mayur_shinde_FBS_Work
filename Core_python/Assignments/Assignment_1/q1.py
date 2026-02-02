#Write a program to calculate the percentage of student based on marks of any 5 subjects.

print("Enter students any 5 subjects marks :")

sub1 = float(input("Enter sub 1 marks : "))
sub2 = float(input("Enter sub 2 marks : "))
sub3 = float(input("Enter sub 3 marks : "))
sub4 = float(input("Enter sub 4 marks : "))
sub5 = float(input("Enter sub 5 marks : "))

Tot = sub1 + sub2 + sub3 + sub4 + sub5
print(f'Total marks : {Tot}')

perc = (Tot / 500) * 100
print(f'Percentage is : {perc}')