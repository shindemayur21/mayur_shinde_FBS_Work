class Student:
    def setData(self, id, name):
        self.ID = id
        self.nm = name
        # print(f'{self.ID = }')
        # print(f'{self.nm = }')

    def getData(self):
        print(f'{self.ID=}')
        print(f'{self.nm=}')


obj1 = Student()
obj1.setData(4, 'Mayur')
obj1.getData()
