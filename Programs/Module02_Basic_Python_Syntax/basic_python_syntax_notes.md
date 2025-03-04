## **Python Basics**
Python is beginner-friendly and follows a simple syntax structure. Here are the fundamental concepts:

### **Python Syntax and Indentation**
Python uses indentation (spaces or tabs) to define blocks of code instead of braces `{}` like in other languages. Proper indentation is crucial, as incorrect indentation leads to errors.

```python
if True:
    print("This is correctly indented")  # Indented block
```

### **Comments in Python**
Comments help in making the code more readable. Python supports:
- **Single-line comments** using `#`
- **Multi-line comments** using triple quotes `'''` or `"""`

```python
# This is a single-line comment
"""
This is a multi-line comment
that spans multiple lines
"""
```

### **Print Statement and String Formatting**
The `print()` function is used to display output in Python. String formatting can be done using:
1. **Basic print function**:
   ```python
   print("Hello, World!")
   ```
2. **Using `format()` method**:
   ```python
   name = "Alice"
   print("Hello, {}!".format(name))
   ```
3. **Using f-strings (Python 3.6+)**:
   ```python
   age = 25
   print(f"I am {age} years old")
   ```
