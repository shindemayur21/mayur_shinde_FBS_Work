class Product:

    # static member
    discount = 10   # 10% discount

    # Constructor
    def __init__(self, pid=0, pname='', price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Constructor called")

    # Destructor
    def __del__(self):
        print("Destructor called for Product")

    # Display method
    def showProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    # Method to apply discount
    def apply_discount(self):
        discount_amount = (self.price * Product.discount) / 100
        self.price -= discount_amount


p1 = Product(1, "Dumbbells", 500, 20)
p1.apply_discount()
p1.showProduct()

p2 = Product()
p2.pid = 2
p2.pname = "Bench"
p2.price = 1500
p2.quantity = 3

p2.apply_discount()
p2.showProduct()
