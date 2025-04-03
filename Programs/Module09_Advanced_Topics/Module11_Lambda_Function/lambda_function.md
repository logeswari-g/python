# **Lambda Function in Python**
A **lambda function** is a small, anonymous function in Python that can have any number of arguments but only one expression. It is used for short, simple functions that do not require a full function definition using `def`.

## **Syntax:**
```python
lambda arguments: expression
```

## **Key Features:**
- Defined using the `lambda` keyword.
- Can take multiple arguments but has only one expression.
- Implicitly returns the result of the expression.
- Used where short-lived functions are needed.

---

## **Use Cases of Lambda Functions**

### **1. Using Lambda with `map()`**
`map()` applies a function to all items in an iterable (e.g., list).

#### **Example: Convert a list of temperatures from Celsius to Fahrenheit**
```python
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
```
**Output:**
```
[32.0, 50.0, 68.0, 86.0, 104.0]
```

---

### **2. Using Lambda with `filter()`**
`filter()` selects items from an iterable based on a condition.

#### **Example: Filtering even numbers from a list**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```
**Output:**
```
[2, 4, 6, 8, 10]
```

---

### **3. Using Lambda with `sorted()` and `key` Parameter**
Lambda functions can be used to customize sorting.

#### **Example: Sorting a list of tuples based on the second value**
```python
employees = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
sorted_employees = sorted(employees, key=lambda x: x[1])
print(sorted_employees)
```
**Output:**
```
[('Charlie', 22), ('Alice', 25), ('Bob', 30)]
```

---

### **4. Using Lambda in `reduce()` from `functools`**
`reduce()` is used to apply a function cumulatively to a sequence.

#### **Example: Finding the product of all elements in a list**
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
```
**Output:**
```
120
```

---

### **5. Using Lambda in Real-Time Web Scraping Example**
In web scraping, lambda functions can be used for quick data transformations.

#### **Example: Extracting and cleaning text from scraped data**
```python
scraped_data = ["\nPrice: $100\n", "  Name: Laptop  ", "\tCategory: Electronics\n"]

cleaned_data = list(map(lambda x: x.strip(), scraped_data))
print(cleaned_data)
```
**Output:**
```
['Price: $100', 'Name: Laptop', 'Category: Electronics']
```
---
