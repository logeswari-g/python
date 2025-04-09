## **1. Introduction to Loops**
Loops in Python allow executing a block of code multiple times. Python provides two main types of loops:
- `for` loop
- `while` loop

---

## **2. for Loop**
The `for` loop is used for iterating over a sequence (such as a list, tuple, dictionary, string, or range).

### **Syntax:**
```python
for variable in sequence:
    # Code block to execute
```

### **Example:**
```python
for num in [1, 2, 3, 4, 5]:
    print(num)
```

### **Using range() in for Loop:**
```python
for i in range(1, 6):
    print(i)
```

---

## **3. while Loop**
The `while` loop executes as long as a specified condition is `True`.

### **Syntax:**
```python
while condition:
    # Code block to execute
```

### **Example:**
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

## **4. Loop Control Statements**
Python provides loop control statements to modify loop execution.

### **break Statement**
The `break` statement terminates the loop completely.
```python
for num in range(1, 6):
    if num == 4:
        break
    print(num)
# Output: 1 2 3
```

### **continue Statement**
The `continue` statement skips the current iteration and moves to the next.
```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# Output: 1 2 4 5
```

### **pass Statement**
The `pass` statement is a placeholder for future code.
```python
for num in range(1, 6):
    if num == 3:
        pass  # Placeholder, does nothing
    print(num)
```

---

## **5. Nested Loops**
A loop inside another loop is called a **nested loop**.

### **Example:**
```python
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")
```

---

## **6. else with Loops**
Python allows an `else` clause in loops, executed when the loop finishes without a `break` statement.

### **Example:**
```python
for num in range(1, 4):
    print(num)
else:
    print("Loop finished without break")
```

---

## **7. Sample Program**
Below is a Python program demonstrating different loop types and control statements.

```python
# Sample program demonstrating loops
print("For Loop Example:")
for i in range(1, 6):
    print(i)

print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\nBreak Statement Example:")
for num in range(1, 6):
    if num == 3:
        break
    print(num)

print("\nContinue Statement Example:")
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

print("\nNested Loop Example:")
for i in range(1, 3):
    for j in range(1, 3):
        print(f"i={i}, j={j}")
```
