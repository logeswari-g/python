# **Complete Notes on Inheritance in Python**

Inheritance is one of the core concepts of Object-Oriented Programming (OOP) in Python. It allows a new class (child or derived class) to inherit properties and methods from an existing class (parent or base class). This promotes **code reusability**, **extensibility**, and **modularity**.

## **1. Types of Inheritance**
Python supports different types of inheritance:

### **1.1 Single Inheritance**
A child class inherits from only one parent class.

```python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

# Creating an object of Dog
d = Dog()
print(d.speak())  # Inherited method
print(d.bark())   # Child class method
```

### **1.2 Multiple Inheritance**
A child class inherits from multiple parent classes.

```python
class Father:
    def skill_father(self):
        return "Father: Good at Mathematics"

class Mother:
    def skill_mother(self):
        return "Mother: Good at Cooking"

class Child(Father, Mother):
    def skill_child(self):
        return "Child: Good at Sports"

c = Child()
print(c.skill_father())  # Inherited from Father
print(c.skill_mother())  # Inherited from Mother
print(c.skill_child())   # Child's own method
```

### **1.3 Multilevel Inheritance**
A class is derived from another derived class.

```python
class Grandparent:
    def grandparent_method(self):
        return "This is Grandparent's method"

class Parent(Grandparent):
    def parent_method(self):
        return "This is Parent's method"

class Child(Parent):
    def child_method(self):
        return "This is Child's method"

c = Child()
print(c.grandparent_method())  # Inherited from Grandparent
print(c.parent_method())       # Inherited from Parent
print(c.child_method())        # Child's own method
```

### **1.4 Hierarchical Inheritance**
Multiple child classes inherit from the same parent class.

```python
class Vehicle:
    def general_info(self):
        return "Vehicles have engines"

class Car(Vehicle):
    def car_info(self):
        return "Cars have 4 wheels"

class Bike(Vehicle):
    def bike_info(self):
        return "Bikes have 2 wheels"

c = Car()
b = Bike()
print(c.general_info())  # Inherited from Vehicle
print(c.car_info())      # Specific to Car
print(b.general_info())  # Inherited from Vehicle
print(b.bike_info())     # Specific to Bike
```

### **1.5 Hybrid Inheritance**
Combination of two or more types of inheritance.

```python
class A:
    def method_A(self):
        return "Method from A"

class B(A):
    def method_B(self):
        return "Method from B"

class C(A):
    def method_C(self):
        return "Method from C"

class D(B, C):
    def method_D(self):
        return "Method from D"

obj = D()
print(obj.method_A())  # Inherited from A
print(obj.method_B())  # Inherited from B
print(obj.method_C())  # Inherited from C
print(obj.method_D())  # Own method
```

## **2. The `super()` Function**
The `super()` function is used to call a method from the parent class.

```python
class Parent:
    def show(self):
        return "Parent method"

class Child(Parent):
    def show(self):
        return super().show() + " and Child method"

c = Child()
print(c.show())  # Output: Parent method and Child method
```

## **3. Method Overriding in Inheritance**
When a method in the child class has the same name as a method in the parent class, it **overrides** the parent method.

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

c = Child()
print(c.greet())  # Output: Hello from Child
```

## **4. The `isinstance()` and `issubclass()` Functions**
- `isinstance(obj, Class)`: Checks if `obj` is an instance of `Class`.
- `issubclass(SubClass, ParentClass)`: Checks if `SubClass` is derived from `ParentClass`.

```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True
print(issubclass(Dog, Animal)) # True
```
