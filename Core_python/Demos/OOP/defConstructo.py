class Mobile:
    def __init__(self, brand='', processor='', storage=0, price=0):
        self.brand = brand
        self.pro = processor
        self.sto = storage
        self.price = price
    
    def getData(self):
        print('Brand :',self.brand)
        print('Processor :',self.pro)
        print('Storage :',self.sto)
        print('Price :',self.price)

m1 = Mobile(storage=5000)
m1.getData()
