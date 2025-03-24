class Fruits:
    def __init__(self, shopname):
        self.shopname = shopname

    def welcome(self):
        print("Welcome to Parent Class - welcome method()")

    def sayhi(self):
        print("Hiiiiiiiiiiiii")

class Apple(Fruits):
    def __init__(abc, count, color, shopname):
        abc.count = count
        abc.color = color
        Fruits.__init__(abc, shopname)

    def welcome(self):
        print("Welcome to Child Class - welcome method()")

# Creating object for parent and accessing the attributes & methods
parentObj = Fruits("ABC")
print(parentObj.shopname) # ABC
parentObj.welcome()

# Creating object for child and accessing the attributes & methods
childObj = Apple(10, "red", "XYZ")
print(childObj.count) # Child class attributes
print(childObj.color) # Child class attributes
print(childObj.shopname) # Parent class attributes
childObj.welcome() # Child class will override parent class method
childObj.sayhi()
