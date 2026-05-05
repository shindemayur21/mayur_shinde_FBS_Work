# 2. Create a derived class from Student as EnggStudent with :
#     a. Data members as :
#     i. Branch
#     ii. InternalMarks
# b. Add the following methods :
#     i. Parameterized constructor
#     ii. Display
#     iii. Accept
#     iv. override Method CalculateRank
#     v. Override __str__ Method

from q1 import Student


class EnggStudent(Student):

    # Parameterized constructor
    def __init__(self, studentId=0, name="", age=0, percentage=0.0,
                 branch="", internalMarks=0):

        # call parent constructor
        super().__init__(studentId, name, age, percentage)

        self.branch = branch
        self.internalMarks = internalMarks

    # Accept method
    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internalMarks = int(input("Enter Internal Marks: "))

    # Display method
    def display(self):
        super().display()
        print("Branch:", self.branch)
        print("Internal Marks:", self.internalMarks)

    # Override CalculateRank
    def calculateRank(self):
        total = self.percentage + (self.internalMarks / 2)

        if total >= 90:
            return "Outstanding"
        elif total >= 75:
            return "Excellent"
        elif total >= 60:
            return "Good"
        elif total >= 50:
            return "Average"
        else:
            return "Poor"

    # Override __str__
    def __str__(self):
        return f"{super().__str__()} - {self.branch} - {self.internalMarks}"


e1 = EnggStudent()

e1.accept()
e1.display()

print(e1)
