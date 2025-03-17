## Introduction to Functions

A function in Python is a block of reusable code designed to perform a specific task. Functions help in modular programming by breaking code into smaller, manageable, and reusable sections.

## Defining a Function

A function is defined using the def keyword followed by a function name and parentheses.

```python
def function_name(parameters):
    """Docstring (optional): Describes the function."""
    # Function body
    return value  # Optional return statement
```

## Method 1: Numbers of Arguments (Positional Arguments)

Functions in Python can accept a fixed number of arguments, which must be passed in a specific order.

### **Example:**
```python
def function_name(arg1, arg2):
    """Docstring (optional): Describes the function."""
    # Function body
    return value  # Optional return statement

result1 = function_name(arg1, arg2)
```

---

## Method 2: Keyword Arguments

With keyword arguments, the position of arguments does not matter as each argument is explicitly assigned a value.

### **Example:**
```python
def function_name(arg2, arg1):
    """Docstring (optional): Describes the function."""
    # Function body
    return value  # Optional return statement

result1 = function_name(arg1 = value, arg2 = value)
```

---

## Method 3: Arbitrary Arguments (`*args`)

Arbitrary arguments allow functions to accept a variable number of arguments, which are treated as a tuple.

### **Example:**
```python
def function_name(*args):
    """Docstring (optional): Describes the function."""
    # Function body
    return value  # Optional return statement

result1 = function_name(value1, value2, value3, value4)
result2 = function_name(value1, value2)
```
---

## Method 4: Keyword Arbitrary Arguments (`**kwargs`)

Using `**kwargs`, functions can accept a variable number of keyword arguments, which are stored as a dictionary.

### **Example:**
```python
def function_name(*kwargs):
    """Docstring (optional): Describes the function."""
    # Function body
    return value  # Optional return statement

result1 = function_name(key1 = value1, key2 = value2, key3 = value3) ## can include keys as needed
```

---

## Method 5: Default Values in Function Arguments

Default values allow functions to be called with fewer arguments by providing default values for some parameters.

### **Example:**
```python
def function_name(arg1, arg2="value"):
    """Docstring (optional): Describes the function."""
    # Function body
    return value  # Optional return statement

result1 = function_name(arg1 = value) ## if arg2 not provided it takes default value
result1 = function_name(arg1 = value, arg2 = "value2") ## if arg2 provided it takes provided value
```
