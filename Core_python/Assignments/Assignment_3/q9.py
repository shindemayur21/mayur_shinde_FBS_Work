# Input marks from user and display grade(eg.First class,Second class ..)

marks = int(input(f'Enter marks : '))

if (marks >= 90):
    print("First Class with distinction")
elif (marks >= 80 and marks <= 90):
    print("First class")
elif (marks >= 70 and marks < 80):
    print("Second class")
elif (marks >= 60 and marks < 70):
    print("Third class")
elif (marks >= 40 and marks < 60):
    print("Third class")
else:
    print("Failed")