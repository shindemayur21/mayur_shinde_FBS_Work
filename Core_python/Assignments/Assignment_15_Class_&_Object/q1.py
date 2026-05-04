# 1. Create a class Book with members as bid,bname,price and author. Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:

    # Constructor (works as parameterized & parameterless)
    def __init__(self, bid=0, bname='', price=0, author=''):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Constructor called")

    # Destructor
    def __del__(self):
        print("Destructor called for Book")

    # Method to display book details
    def showBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)


b1 = Book(1, "Core Python", 200, "abc")
b1.showBook()

b2 = Book()
b2.bid = 2
b2.bname = "Advance Python"
b2.price = 1500
b2.author = "xyz"
b2.showBook()
