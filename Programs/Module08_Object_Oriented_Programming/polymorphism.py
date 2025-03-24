class Ednue:
    def welcome(self):
        raise NotImplementedError("Implement a method in sub class")

# Base class - Inherits parent class - Ednue
class PythonBatch(Ednue):
    # Method Overriding
    def welcome(self):
        print("Welcome to Python Batch")

# Base class - Inherits parent class - Ednue
class JavaBatch(Ednue):
    # Method Overriding
    def welcome(self):
        print("Welcome to Python Batch")

pythonObj = PythonBatch()
pythonObj.welcome()

javaObj = JavaBatch()
javaObj.welcome()

ednueObj = Ednue()
# ednueObj.welcome() # NotImplementedError: Implement a method in sub class

print ( 'abc' * 20 )

# Method Overloading
# A definition accepts more than one datatype of argument
# and functionality is differed based on it
print(len("Ednue")) # 5
print(len([10,20,30,40])) # 4
