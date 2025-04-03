# **Polymorphism in Python (OOP Concept)**

## **What is Polymorphism?**
Polymorphism is a fundamental concept in Object-Oriented Programming (OOP) that allows the **same method or operator** to work differently based on the object or data type it is applied to. This improves **code flexibility, reusability, and scalability**.

---

## **Types of Polymorphism in Python**
1. **Method Overriding (Runtime Polymorphism)**
2. **Method Overloading (Compile-time Polymorphism)**
3. **Operator Overloading**

---

## **1. Method Overriding (Runtime Polymorphism)**
Method Overriding occurs when a **subclass provides a specific implementation** of a method that is already defined in its parent class.

### **Example: Animal Sound Simulation**
```python
class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Function demonstrating polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Creating objects of subclasses
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
```

### **Explanation:**
- The `Animal` class has a method `make_sound()`.
- The `Dog` and `Cat` classes override the method to provide their own implementations.
- The function `animal_sound()` demonstrates **runtime polymorphism**, as it works with different subclasses.

---

## **2. Method Overloading (Compile-Time Polymorphism)**
Python **does not support method overloading natively**, but we can achieve it using **default arguments, `*args`, or multiple dispatch**.

### **Example: Adding Numbers with Different Arguments**
```python
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

math_op = MathOperations()
print(math_op.add(5))        # Output: 5
print(math_op.add(5, 10))    # Output: 15
print(math_op.add(5, 10, 15)) # Output: 30
```

### **Explanation:**
- The `add()` method works with **one, two, or three arguments**.
- Default values allow us to **mimic method overloading**.

---

## **3. Operator Overloading**
Python allows **overloading operators** (e.g., `+`, `-`, `*`, etc.) by defining special dunder methods.

### **Example: Overloading `+` Operator for a Custom Class**
```python
class Box:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        return Box(self.weight + other.weight)

    def __str__(self):
        return f"Box with weight {self.weight}kg"

box1 = Box(10)
box2 = Box(15)
box3 = box1 + box2  # Calls __add__ method

print(box3)  # Output: Box with weight 25kg
```

### **Explanation:**
- The `+` operator is overloaded using `__add__`, allowing us to **add two `Box` objects** like numbers.
- The `__str__` method is overridden to **print a custom string representation**.

---
