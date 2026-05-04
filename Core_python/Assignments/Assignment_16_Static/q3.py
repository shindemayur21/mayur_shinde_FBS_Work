# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:

    # static base discount 10%
    step = 10

    # Constructor (parameterized + parameterless)
    def __init__(self, sid=None, sname=None, stype=None, price=0):
        self.sid = sid
        self.sname = sname
        self.type = stype
        self.base_price = price   # store original price
        self.size = None
        self.price = price
        print("Constructor called")

    # Destructor
    def __del__(self):
        print("Destructor called for Shirt")

    # Apply price based on size
    def set_size(self, size):
        self.size = size.lower()

        if self.size == "small":
            self.price = self.base_price
        elif self.size == "medium":
            self.price = self.base_price + (self.base_price * Shirt.step / 100)
        elif self.size == "large":
            self.price = self.base_price + (2 * self.base_price * Shirt.step / 100)
        elif self.size == "xlarge":
            self.price = self.base_price + (3 * self.base_price * Shirt.step / 100)
        else:
            print("Invalid size")

    # Display method
    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Price:", self.price)


s1 = Shirt(1, "Nike", "Formal", 1000)

s1.set_size("small")
s1.showShirt()

s1.set_size("medium")
s1.showShirt()

s1.set_size("large")
s1.showShirt()

s1.set_size("xlarge")
s1.showShirt()
