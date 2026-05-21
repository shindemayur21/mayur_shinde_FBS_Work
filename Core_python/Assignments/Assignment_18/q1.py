# Create a class Complex Number with data members as real and imag and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:
    # Constructor
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print("Constructor called")

    # Overloading + operator
    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imag + other.imag
        )

    # Overloading - operator
    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imag - other.imag
        )

    # String representation for printing
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    # Destructor
    def __del__(self):
        print("Destructor called")


# Creating objects
c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

# Addition
c3 = c1 + c2
print("Addition:", c3)

# Subtraction
c4 = c1 - c2
print("Subtraction:", c4)