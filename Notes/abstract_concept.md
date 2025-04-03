# **Abstraction in Python (OOP Concept)**

Abstraction is one of the core principles of Object-Oriented Programming (OOP). It is used to hide implementation details from the user and only show the necessary functionalities. This makes the code cleaner and reduces complexity.

## **Python Example**
Using the `ABC` module and `@abstractmethod` decorator from the `abc` module:

```python
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method, must be implemented by subclasses
    
    @abstractmethod
    def stop_engine(self):
        pass

# Concrete Class (inherits from abstract class)
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    
    def stop_engine(self):
        print("Car engine stopped")

# Trying to instantiate an abstract class will raise an error
# vehicle = Vehicle()  # This will raise an error

# Creating an object of the concrete class
car = Car()
car.start_engine()  # Output: Car engine started
car.stop_engine()   # Output: Car engine stopped
```
---

# **Real-World Example of Abstraction in Python**

### **Use Case: Online Payment System**
- The user doesn't need to know how each payment method processes transactions internally.
- The user only interacts with a common interface (`Payment` class) to **make a payment**.

## **Python Implementation:**

```python
from abc import ABC, abstractmethod

# Abstract Class (Defines the common interface)
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Abstract method for processing payment"""
        pass

# Concrete Class 1: Credit Card Payment
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ₹{amount}")

# Concrete Class 2: PayPal Payment
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ₹{amount}")

# Concrete Class 3: UPI Payment
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount}")

# Using the abstraction
def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

# Create objects of concrete classes
credit_card = CreditCardPayment()
paypal = PayPalPayment()
upi = UPIPayment()

# Make payments using different methods
make_payment(credit_card, 1000)  # Output: Processing credit card payment of ₹1000
make_payment(paypal, 500)        # Output: Processing PayPal payment of ₹500
make_payment(upi, 200)           # Output: Processing UPI payment of ₹200
```
