class Student:
    count = 0

    def __init__(self, id, name):
        Student.count += 1
        self.ID = id
        self.nm = name

    def getData(self):
        print(f'{self.ID=}')
        print(f'{self.nm=}')

    def totalCount():
        return Student.count


obj1 = Student(4, 'Mayur')
obj2 = Student(5, 'Shinde')
obj3 = Student(2, 'Mayur1')

print(Student.totalCount())
