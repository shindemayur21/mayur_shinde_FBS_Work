from SY.symarks import SYMarks
from TY.tymarks import TYMarks


class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_result(self):

        # Add SY Computer marks and TY Theory marks
        total = self.sy_marks.computer_total + self.ty_marks.theory

        percentage = total / 2

        # Grade Calculation
        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        # Display Result
        print("\n----- STUDENT RESULT -----")
        print("Roll Number :", self.roll_no)
        print("Name        :", self.name)

        print("\nSY Marks")
        print("Computer    :", self.sy_marks.computer_total)
        print("Maths       :", self.sy_marks.maths_total)
        print("Electronics :", self.sy_marks.electronics_total)

        print("\nTY Marks")
        print("Theory      :", self.ty_marks.theory)
        print("Practical   :", self.ty_marks.practical)

        print("\nTotal of SY Computer + TY Theory :", total)
        print("Percentage :", percentage)
        print("Grade      :", grade)


# Creating Objects
sy = SYMarks(80, 75, 70)
ty = TYMarks(65, 60)

# Containment
student = Student(101, "Rahul", sy, ty)

# Display Result
student.calculate_result()
