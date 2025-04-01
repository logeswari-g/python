# Normal Attribute
bankname = "HDFC Bank"

# Normal definition
def welcome():
    print("Welcome to HDFC Bank!")

# syntax:
# class <classname>
class User:
    # Class Variable (Optional)
    branch = "Eagattur"

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

print(bankname)
# print(branch) # NameError: name 'branch' is not defined
welcome()

# Creating object for class
userObj = User("Devid", "9876543210");
print(userObj.accname) # Accessing instance variable
print(userObj.branch) # Accessing class variable
userObj.printaccdetails(100) # # Accessing class definition
