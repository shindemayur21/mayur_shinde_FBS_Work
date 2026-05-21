# Create a class Distance with data members as km,m and cm and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:
    # Constructor
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self.normalize()
        print("Constructor called")

    # Method to normalize values
    def normalize(self):
        # Convert cm to m
        self.m += self.cm // 100
        self.cm = self.cm % 100

        # Convert m to km
        self.km += self.m // 1000
        self.m = self.m % 1000

    # Overloading + operator
    def __add__(self, other):
        return Distance(
            self.km + other.km,
            self.m + other.m,
            self.cm + other.cm
        )

    # Overloading - operator
    def __sub__(self, other):
        total_cm1 = (self.km * 1000 * 100) + (self.m * 100) + self.cm
        total_cm2 = (other.km * 1000 * 100) + (other.m * 100) + other.cm

        diff = total_cm1 - total_cm2

        km = diff // (1000 * 100)
        diff %= (1000 * 100)

        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)

    # String representation
    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    # Destructor
    def __del__(self):
        print("Destructor called")


# Creating objects
d1 = Distance(2, 500, 75)
d2 = Distance(1, 800, 50)

# Addition
d3 = d1 + d2
print("Addition:", d3)

# Subtraction
d4 = d1 - d2
print("Subtraction:", d4)