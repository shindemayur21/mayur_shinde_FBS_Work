import pickle
import os

# Create Employee Class


class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("Employee ID :", self.eid)
        print("Employee Name :", self.ename)
        print("Basic Salary :", self.basic)
        print("-" * 30)


FILENAME = "employee.dat"


# Add Record
def add_record():
    f = open(FILENAME, "ab")

    eid = int(input("Enter Employee ID : "))
    ename = input("Enter Employee Name : ")
    basic = float(input("Enter Basic Salary : "))

    emp = Emp(eid, ename, basic)

    pickle.dump(emp, f)

    f.close()
    print("Record Added Successfully")


# Display All Records
def display_records():
    if not os.path.exists(FILENAME):
        print("File does not exist")
        return

    f = open(FILENAME, "rb")

    print("\nEmployee Records")
    print("-" * 30)

    try:
        while True:
            emp = pickle.load(f)
            emp.display()

    except EOFError:
        f.close()


# Search Record
def search_record():
    if not os.path.exists(FILENAME):
        print("File does not exist")
        return

    search_id = int(input("Enter Employee ID to Search : "))

    f = open(FILENAME, "rb")
    found = False

    try:
        while True:
            emp = pickle.load(f)

            if emp.eid == search_id:
                print("Record Found\n")
                emp.display()
                found = True
                break

    except EOFError:
        if not found:
            print("Record Not Found")

    f.close()


# Delete Record
def delete_record():
    if not os.path.exists(FILENAME):
        print("File does not exist")
        return

    delete_id = int(input("Enter Employee ID to Delete : "))

    f = open(FILENAME, "rb")
    temp = open("temp.dat", "wb")

    found = False

    try:
        while True:
            emp = pickle.load(f)

            if emp.eid != delete_id:
                pickle.dump(emp, temp)
            else:
                found = True

    except EOFError:
        pass

    f.close()
    temp.close()

    os.remove(FILENAME)
    os.rename("temp.dat", FILENAME)

    if found:
        print("Record Deleted Successfully")
    else:
        print("Record Not Found")


# Edit Record
def edit_record():
    if not os.path.exists(FILENAME):
        print("File does not exist")
        return

    edit_id = int(input("Enter Employee ID to Edit : "))

    f = open(FILENAME, "rb")
    temp = open("temp.dat", "wb")

    found = False

    try:
        while True:
            emp = pickle.load(f)

            if emp.eid == edit_id:
                print("Existing Record")
                emp.display()

                emp.ename = input("Enter New Name : ")
                emp.basic = float(input("Enter New Salary : "))

                found = True

            pickle.dump(emp, temp)

    except EOFError:
        pass

    f.close()
    temp.close()

    os.remove(FILENAME)
    os.rename("temp.dat", FILENAME)

    if found:
        print("Record Updated Successfully")
    else:
        print("Record Not Found")


# Main Menu
while True:
    print("\n===== EMPLOYEE MENU =====")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        add_record()

    elif choice == 2:
        search_record()

    elif choice == 3:
        delete_record()

    elif choice == 4:
        edit_record()

    elif choice == 5:
        display_records()

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
