from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    # abstract method using decorator (@abstractmethod)
    @abstractmethod
    def displayNoOfSides(self):
        pass

class Square(Shape):
    def displayNoOfSides(self):
        print("Square has 4 sides")

class Triangle(Shape):
    def displayNoOfSides(self):
        print("Square has 3 sides")

class Hexagon(Shape):
    def displaySides(self):
        print("Square has 6 sides")

squareObj = Square()
squareObj.displayNoOfSides()

triangleObj = Triangle()
triangleObj.displayNoOfSides()

hexagonObj = Hexagon()
# hexagonObj.displayNoOfSides() # TypeError: Can't instantiate abstract class Hexagon without an implementation for abstract method 'displayNoOfSides'
