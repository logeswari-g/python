## **1. List Comprehension**
List comprehension is a compact way to create lists in Python.

### **Syntax:**
```python
[expression for item in iterable if condition]
```

### **Example:**
```python
# Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### **Using If Condition in List Comprehension**
```python
# Get even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]
```

---

## **2. Dictionary Comprehension**
Dictionary comprehension provides a way to create dictionaries dynamically.

### **Syntax:**
```python
{key_expression: value_expression for item in iterable if condition}
```

### **Example:**
```python
# Create a dictionary with numbers and their squares
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### **Using If Condition in Dictionary Comprehension**
```python
# Create a dictionary of even numbers and their cubes
cubes_dict = {x: x**3 for x in range(1, 11) if x % 2 == 0}
print(cubes_dict)  # Output: {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}
```
