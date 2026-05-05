# 1. Create a class Student with following
# a. data members :
#    i. StudentId
#    ii. Name
#    iii. Age
#    iv. Percentage
# b. Add the following methods :
#    i. Parameterized constructor
#    ii. Display
#    iii. Accept
#    iv. Method CalculateRank
#    v. Override __str__ Method

class Student:

    # Parameterized constructor
    def __init__(self, studentId=0, name="", age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    # Accept method (input from user)
    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    # Display method
    def display(self):
        print("Student ID:", self.studentId)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)
        print("Rank:", self.calculateRank())

    # Calculate Rank method
    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        elif self.percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    # Override __str__ method
    def __str__(self):
        return f"{self.studentId} - {self.name} - {self.age} - {self.percentage}%"
    
s1 = Student(101, "Amit", 20, 82.5)
s1.display()

print(s1)   # calls __str__

s2 = Student()
s2.accept()
s2.display()