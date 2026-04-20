class Mobile:
    def __init__(self, brand, processor, storage, price):
        self.brand = brand
        self.pro = processor
        self.sto = storage
        self.price = price

    def getData(self):
        # return f'Brand : {self.brand}'
        print('Brand :', self.brand)
        # print('Processor :', self.pro)
        # print('Storage :', self.sto)
        # print('Price :', self.price)


m1 = Mobile('Samsung','snapdragon','1 TB',150000)
m1.getData()
