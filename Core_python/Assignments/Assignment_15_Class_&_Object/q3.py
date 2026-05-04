# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:

    # Constructor (parameterized + parameterless)
    def __init__(self, sid=0, sname='', stype='', price=0, size=''):
        self.sid = sid
        self.sname = sname
        self.type = stype
        self.price = price
        self.size = size
        print("Constructor called")

    # Destructor
    def __del__(self):
        print("Destructor called for Shirt")

    # Display method
    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)


s1 = Shirt(1, "Peter England", "Formal", 1499, "L")
s1.showShirt()

s2 = Shirt()
s2.sid = 2
s2.sname = "Allen Solly"
s2.type = "Casual"
s2.price = 1199
s2.size = "M"

s2.showShirt()

del s1
