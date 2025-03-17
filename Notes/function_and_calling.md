1. Introduction to Functions

A function in Python is a block of reusable code designed to perform a specific task. Functions help in modular programming by breaking code into smaller, manageable, and reusable sections.

2. Defining a Function

A function is defined using the def keyword followed by a function name and parentheses.

```
def function_name(parameters):
    """Docstring (optional): Describes the function."""
    # Function body
    return value  # Optional return statement
```

## ** Method 1: Numbers of Arguments (Positional Arguments)**

Functions in Python can accept a fixed number of arguments, which must be passed in a specific order.

### **Example:**
```python
def addition(num1, num2):
    sum = num1 + num2
    return sum

print("****** Numbers of Arguments ******")
result1 = addition(10, 20)
print(result1)  # Output: 30
```

---

## ** Method 2: Keyword Arguments**

With keyword arguments, the position of arguments does not matter as each argument is explicitly assigned a value.

### **Example:**
```python
def addition(num2, num1):  # Position of arguments is changed
    sum = num1 + num2
    return sum

print("****** Keyword Arguments ******")
result2 = addition(num1=10, num2=20)
print(result2)  # Output: 30
```

---

## ** Method 3: Arbitrary Arguments (`*args`)**

Arbitrary arguments allow functions to accept a variable number of arguments, which are treated as a tuple.

### **Example:**
```python
def addition(*nums):  # nums = (10, 20, 30, 40)
    value = ""
    for num in nums:
        value += str(num)
    print(value)  # Output: "10203040"
    return sum(nums)  # Using Python built-in sum() function

result3 = addition(10, 20, 30, 40)
print(result3)  # Output: 100
result4 = addition(10, 20, 30, 40, 50)
print(result4)  # Output: 150
```
---

## ** Method 4: Keyword Arbitrary Arguments (`**kwargs`)**

Using `**kwargs`, functions can accept a variable number of keyword arguments, which are stored as a dictionary.

### **Example:**
```python
def laptopCount(**values):
    print(values)  # Prints dictionary of keyword arguments
    print(values['name1'])  # Accessing specific key
    print(values.get('name5'))  # Accessing non-existing key safely

laptopCount(name1="Dell", count1=10,
            name2="Apple", count2=20,
            name3="Lenovo", count3=30,
            name4="Asus", count4=5)

### **Output:**

{'name1': 'Dell', 'count1': 10, 'name2': 'Apple', 'count2': 20, 'name3': 'Lenovo', 'count3': 30, 'name4': 'Asus', 'count4': 5}
Dell
None  # 'name5' does not exist, so None is returned
```

---

## ** Method 5: Default Values in Function Arguments**

Default values allow functions to be called with fewer arguments by providing default values for some parameters.

### **Example:**
```python
def defaultValues(x, y="Ednue"):
    print(x)
    print(y)

defaultValues(x=10)  # Output: 10, Ednue
defaultValues(x=20, y="TCS")  # Output: 20, TCS
defaultValues(20, "TCS")  # Output: 20, TCS
```
