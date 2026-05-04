# 2. Create a class Product with members as pid,pname,price and quantity .
# Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook


class Product:

    # Constructor (works as parameterized & parameterless)
    def __init__(self, pid=0, pname='', price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Constructor called")

    # Destructor
    def __del__(self):
        print("Destructor called for Product")

    # Method to display book details
    def showProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


b1 = Product(1, "Dumbells", 500, 20)
b1.showProduct()

b2 = Product()
b2.bid = 2
b2.bname = "Bench"
b2.price = 1500
b2.author = 3
b2.showProduct()

del b1