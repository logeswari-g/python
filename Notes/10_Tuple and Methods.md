## **1. Introduction to Tuples**
A **tuple** in Python is an **ordered**, **immutable**, and **indexed** collection that can hold multiple items.

### **Example:**
```python
tuple_example = (1, 2, 3, 4, 5)
print(tuple_example)  # Output: (1, 2, 3, 4, 5)
```

---

## **2. Characteristics of Tuples**
- **Ordered**: Elements have a fixed order.
- **Immutable**: Cannot be changed after creation.
- **Allows Duplicates**: Can contain duplicate elements.
- **Indexed**: Elements can be accessed using an index.

---

## **3. Creating Tuples**
Tuples can be created using parentheses `()` or without them.

```python
tuple1 = (1, 2, 3)
tuple2 = "apple", "banana", "cherry"  # Parentheses optional

print(tuple1)  # Output: (1, 2, 3)
print(tuple2)  # Output: ('apple', 'banana', 'cherry')
```

A tuple with a single element must include a trailing comma:
```python
tuple_single = (5,)
print(type(tuple_single))  # Output: <class 'tuple'>
```

---

## **4. Accessing Tuple Elements**
### **Using Indexing**
```python
tuple1 = (10, 20, 30)
print(tuple1[1])  # Output: 20
```

### **Using Slicing**
```python
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[1:4])  # Output: (20, 30, 40)
```

### **Negative Indexing**
```python
tuple1 = (10, 20, 30, 40)
print(tuple1[-1])  # Output: 40
```

---

## **5. Tuple Methods**
| Method | Description | Example |
|--------|-------------|---------|
| `count(value)` | Returns the number of times a value appears in the tuple. | `t = (1, 2, 2, 3); print(t.count(2)) # 2` |
| `index(value)` | Returns the first index of the specified value. | `t = (10, 20, 30); print(t.index(20)) # 1` |

---

## **6. Iterating Over Tuples**
```python
tuple1 = ("apple", "banana", "cherry")
for item in tuple1:
    print(item)
```

---

## **7. Tuple Unpacking**
Tuple unpacking allows assigning values to multiple variables in one step.

```python
tuple1 = ("John", 25, "Engineer")
name, age, profession = tuple1
print(name, age, profession)  # Output: John 25 Engineer
```
---

## **9. Sample Program**
Below is a sample Python program demonstrating various tuple operations:

```python
# Sample program demonstrating tuple methods
tuple1 = (10, 20, 30, 40, 50)

# Accessing elements
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])

# Counting occurrences
tuple2 = (1, 2, 2, 3, 4, 2)
print("Count of 2:", tuple2.count(2))

# Finding index
print("Index of 30:", tuple1.index(30))

# Tuple unpacking
t = ("Alice", 28, "Doctor")
name, age, profession = t
print(f"Name: {name}, Age: {age}, Profession: {profession}")
```
