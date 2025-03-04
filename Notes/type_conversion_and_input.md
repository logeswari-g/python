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
