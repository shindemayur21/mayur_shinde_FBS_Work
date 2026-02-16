#  Enter number of students from user. For those many students accept marks of 5  
# subject marks from user and calculate percentage. Display all percentage and  
# average percentage of students.

n = int(input("Enter no of students : "))

for i in range(1, n+1):
    marks = float(input(f'Enter 5 subject marks for Studetn {i} : '))
    perc = (marks / 500) * 100
    print(f'Percentage of {i}st Student is {perc:.2f}')