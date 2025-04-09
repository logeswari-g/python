# Exception Handling in Python

Exception handling in Python is used to manage runtime errors and prevent program crashes. Python provides the `try-except` block to handle exceptions gracefully.

## **Types of Errors in Python**
1. **Syntax Errors** – Errors in code structure.
   ```python
   print("Hello"  # Missing closing parenthesis
   ```
2. **Exceptions** – Errors during execution.
   ```python
   x = 10 / 0  # ZeroDivisionError
   ```

## **Handling Exceptions using `try-except`**
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## **Catching Multiple Exceptions**
```python
try:
    num = int("abc")
except (ValueError, TypeError) as e:
    print("Error occurred:", e)
```

## **Using `else` Block**
```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful:", x)
```

## **Using `finally` Block**
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
```
- The `finally` block always executes, regardless of exceptions.

## **Raising Exceptions using `raise`**
```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Allowed"

try:
    print(check_age(16))
except ValueError as e:
    print("Error:", e)
```

## **Custom Exceptions**
```python
class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative number error: {value} is not allowed")

def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    return f"{number} is positive"

# Handling the exception
try:
    print(check_positive(-5))
except NegativeNumberError as e:
    print("Caught an exception:", e)
```
