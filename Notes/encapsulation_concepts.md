# **Encapsulation in Python**

**Encapsulation** is one of the four fundamental OOP concepts, and it refers to the bundling of data (attributes) and the methods that operate on that data into a single unit, or class. Additionally, encapsulation restricts access to certain details of an object's state and behavior, making it more secure.

## **Access Modifiers or specifiers in Python**
Python doesn't have strict access control like some other languages (e.g., Java or C++), but it uses conventions to indicate access levels:

- **Public**: Attributes or methods that are accessible from anywhere in the program.
    - Defined without any underscores (`variable_name`).

- **Protected**: Attributes or methods intended to be used only within the class and its subclasses.
    - Defined with a single leading underscore (`_variable_name`).

- **Private**: Attributes or methods intended to be used only within the class.
    - Defined with double leading underscores (`__variable_name`).

## **3. Example of Encapsulation in Python**

### **Public Example**
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute
    
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

# Creating an object
person = Person("Alice", 30)
print(person.greet())  # Accessible directly
print(person.name())  # Accessible directly
```

### **Protected Example**
```python
class Car:
    def __init__(self, brand, model):
        self._brand = brand  # Protected attribute
        self._model = model  # Protected attribute
    
    def show_details(self):
        return f"Car: {self._brand} {self._model}"

# Creating an object
car = Car("Tesla", "Model 3")
print(car.show_details())  # Accessible directly, but intended for internal use
```

### **Private Example**
```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. Current balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def get_balance(self):
        return self.__balance

# Creating an object
account = BankAccount("John", 5000)
account.deposit(1000)
print(account.get_balance())  # Access via method
# print(account.__balance)    # Will raise an AttributeError
```
