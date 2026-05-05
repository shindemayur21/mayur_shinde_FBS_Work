# 3. Create a class MedicalStudent inherited from Student with following:
#     i. Data members :Specialization
#     ii. MarksOfInternship
# b. Add the following methods :
#     i. Parameterized constructor
#     ii. Display
#     iii. Accept
#     iv. override Method CalculateRank
#     v. Override __str__ Method

from q1 import Student


class MedicalStudent(Student):

    # Parameterized constructor
    def __init__(self, studentId=0, name="", age=0, percentage=0.0,
                 specialization="", marksOfInternship=0):

        # call parent constructor
        super().__init__(studentId, name, age, percentage)

        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    # Accept method
    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = int(input("Enter Internship Marks: "))

    # Display method
    def display(self):
        super().display()
        print("Specialization:", self.specialization)
        print("Internship Marks:", self.marksOfInternship)

    # Override CalculateRank
    def calculateRank(self):
        total = self.percentage + (self.marksOfInternship / 2)

        if total >= 90:
            return "Top Performer"
        elif total >= 75:
            return "Excellent"
        elif total >= 60:
            return "Good"
        elif total >= 50:
            return "Average"
        else:
            return "Needs Improvement"

    # Override __str__
    def __str__(self):
        return f"{super().__str__()} - {self.specialization} - {self.marksOfInternship}"


m1 = MedicalStudent()

m1.accept()
m1.display()

print(m1)
