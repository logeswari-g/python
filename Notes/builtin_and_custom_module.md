# Python Modules and Packages

## **1. Modules**
A **module** is simply a Python file (`.py`) that contains reusable code such as functions, classes, and variables. Modules help in organizing code logically.

### **Creating a Module**
Create a file named `my_module.py`:
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"
```

### **Using a Module**
Import and use it in another script:
```python
import my_module
print(my_module.greet("Alice"))
```

### **Different Ways to Import a Module**
1. **Using `import`**
   ```python
   import my_module
   print(my_module.greet("Bob"))
   ```
2. **Using `from ... import`**
   ```python
   from my_module import greet
   print(greet("Charlie"))
   ```
3. **Using `import as` (aliasing)**
   ```python
   import my_module as mm
   print(mm.greet("Dave"))
   ```
4. **Using `*` (importing everything)**
   ```python
   from my_module import *
   print(greet("Eve"))
   ```

## **2. Built-in Modules**
Python comes with several built-in modules that provide useful functionality without needing additional installation. These modules help in performing various tasks such as system operations, mathematical computations, handling data formats, and networking.

### **Common Built-in Modules**
1. **sys** – Provides system-specific functions and parameters.
   ```python
   import sys
   print(sys.version)
   ```

2. **os** – Allows interaction with the operating system.
   ```python
   import os
   print(os.getcwd())
   ```

3. **math** – Provides mathematical functions.
   ```python
   import math
   print(math.sqrt(16))
   ```

4. **random** – Generates random numbers.
   ```python
   import random
   print(random.randint(1, 10))
   ```

5. **datetime** – Handles date and time operations.
   ```python
   import datetime
   print(datetime.datetime.now())
   ```

6. **json** – Works with JSON data.
   ```python
   import json
   data = {'name': 'Alice', 'age': 25}
   json_data = json.dumps(data)
   print(json_data)
   ```

7. **re** – Supports regular expressions.
   ```python
   import re
   match = re.search(r'\d+', 'The number is 42')
   print(match.group())
   ```

8. **urllib** – Handles URL-related tasks.
   ```python
   import urllib.request
   response = urllib.request.urlopen('https://www.example.com')
   print(response.status)
   ```

9. **collections** – Provides specialized container datatypes.
   ```python
   from collections import Counter
   print(Counter([1, 2, 2, 3, 3, 3]))
   ```

10. **itertools** – Implements iterator building tools.
    ```python
    import itertools
    for item in itertools.permutations([1, 2, 3]):
        print(item)
    ```

## **3. Packages**
A **package** is a collection of modules stored in a directory. It allows for better organization of large codebases.

### **Structure of a Package**
```
my_package/
|-- __init__.py  (makes the directory a package)
|-- module1.py
|-- module2.py
```
- The `__init__.py` file can be empty or contain initialization code for the package.

### **Creating a Package**
Create a directory `my_package/` and add these files:

#### **module1.py**
```python
# my_package/module1.py
def add(a, b):
    return a + b
```

#### **module2.py**
```python
# my_package/module2.py
def multiply(a, b):
    return a * b
```

#### **__init__.py**
```python
# my_package/__init__.py
from .module1 import add
from .module2 import multiply
```

### **Using a Package**
```python
import my_package

print(my_package.add(2, 3))       # Output: 5
print(my_package.multiply(2, 3))  # Output: 6
```

### **4. Locating Modules and Packages**
Python looks for modules and packages in the following locations:
- Current working directory
- Directories listed in `sys.path`
- Python standard library
- Installed third-party packages

To check the module search paths:
```python
import sys
print(sys.path)
```

## **5. Key Differences Between Modules and Packages**
| Feature    | Module | Package |
|------------|--------|---------|
| Definition | A single `.py` file | A directory containing multiple modules |
| Purpose | Organizes code into a single file | Organizes related modules together |
| Example | `math.py` | `numpy`, `pandas` |

## **6. Summary**
- **Modules** are single `.py` files containing reusable code.
- **Built-in modules** come pre-installed with Python.
- **Custom modules** are user-defined `.py` files.
- **Packages** are directories containing multiple modules with an `__init__.py` file.
- **Different import methods** provide flexibility in using modules and packages.
