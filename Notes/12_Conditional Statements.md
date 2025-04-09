## **1. Introduction to Conditional Statements**
Conditional statements in Python allow the execution of code based on conditions. The primary conditional statements include `if`, `if-else`, `if-elif-else`, nested conditions, and ternary conditions.

---

## **2. if Statement**
The `if` statement executes a block of code only if a specified condition is `True`.

### **Syntax:**
```python
if condition:
    # Code block to execute if condition is True
```

### **Example:**
```python
num = 10
if num > 0:
    print("Positive Number")
```

---

## **3. if-else Statement**
The `if-else` statement executes one block if the condition is `True` and another block if it is `False`.

### **Syntax:**
```python
if condition:
    # Code block if condition is True
else:
    # Code block if condition is False
```

### **Example:**
```python
num = -5
if num > 0:
    print("Positive Number")
else:
    print("Negative Number")
```

---

## **4. if-elif-else Statement**
The `if-elif-else` statement allows checking multiple conditions.

### **Syntax:**
```python
if condition1:
    # Code block if condition1 is True
elif condition2:
    # Code block if condition2 is True
else:
    # Code block if no conditions are True
```

### **Example:**
```python
num = 0
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
```

---

## **5. Nested if Statement**
A nested `if` statement is an `if` condition inside another `if` condition.

### **Syntax:**
```python
if condition1:
    if condition2:
        # Code block if both conditions are True
```

### **Example:**
```python
num = 15
if num > 0:
    print("Positive Number")
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
```

---

## **6. Ternary Condition (Conditional Expression)**
Python supports a shorthand way of writing `if-else` statements using the **ternary operator**.

### **Syntax:**
```python
value_if_true if condition else value_if_false
```

### **Example:**
```python
num = 10
result = "Positive" if num > 0 else "Negative"
print(result)  # Output: Positive
```

---

## **7. Sample Program**
Below is a Python program that demonstrates various conditional statements:

```python
# Example program using different conditional statements
age = int(input("Enter your age: "))

# if-elif-else statement
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Nested if statement
if age >= 18:
    print("You are eligible to vote.")
    if age >= 21:
        print("You are also eligible to marry.")

# Ternary operator
status = "Minor" if age < 18 else "Adult"
print("Your status:", status)
```
