# OOP:
#     - Class - Its a template/blueprint of an object
#     - Objects - Instance of class
#
#     - Encapsulation
#     - Inheritance
#     - Abstraction
#     - Polymorphism

# Normal Attribute
bankname = "HDFC Bank"

# Normal definition
def welcome():
    print("Welcome to HDFC Bank!")

# syntax:
# class <classname>
class user:
    # Class Variable (Optional)
    branch = "Egattur"

    # def __init__(self):
    #     pass

    # Contructor method (Optional)
    def __init__(self, accname, accno):
        # Instance Variable
        self.accname = accname
        self.accno = accno

    # class definition
    def printaccdetails(self, accbal):
        print(f"Account no of {self.accname} is {self.accno} and account balance is {accbal}")
