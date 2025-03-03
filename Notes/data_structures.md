## **Variables and Assignments**
Variables store data and can be assigned dynamically in Python:
```python
x = 10      # Integer
name = "Bob" # String
pi = 3.14   # Float
is_active = True # Boolean
```
Python allows multiple assignments:
```python
a, b, c = 1, 2, 3
```

### **Basic Data Types**
Python has built-in data types:
- `int` (Integer) → Whole numbers (e.g., `10`, `-5`)
- `float` (Floating Point) → Decimal numbers (e.g., `3.14`, `-2.5`)
- `str` (String) → Text (e.g., `'hello'`, `"Python"`)
- `bool` (Boolean) → `True` or `False`

Example:
```python
num = 42        # int
decimal = 3.14  # float
text = "Hello"  # str
flag = False    # bool
```

### **Type Conversion and Casting**
You can convert between different data types using typecasting:
```python
x = 5           # int
y = float(x)    # Convert to float
z = str(x)      # Convert to string
b = bool(x)     # Convert to boolean
```
Example:
```python
num_str = "123"
num_int = int(num_str)  # Converts string to integer
```

### **Basic Input and Output**
Python uses `input()` to take user input and `print()` to display output.
```python
name = input("Enter your name: ")
print("Hello,", name)
```
By default, `input()` returns a string, so you may need to convert it:
```python
age = int(input("Enter your age: "))
print("You are", age, "years old")
```
