## **Data Structures in Python**

### **Lists**
A list is an ordered, mutable collection of elements. It can hold items of different data types.

#### **Characteristics:**
- Ordered (maintains the sequence of elements)
- Mutable (can be changed after creation)
- Allows duplicate elements

#### **Example:**
```python
my_list = [1, 2, 3, "apple", 4.5]
my_list.append("banana")  # Adding an element
print(my_list)
```

---

### **Tuples**
A tuple is an ordered, immutable collection of elements. It is similar to a list but cannot be modified after creation.

#### **Characteristics:**
- Ordered
- Immutable (cannot be changed after creation)
- Allows duplicate elements

#### **Example:**
```python
my_tuple = (1, 2, 3, "apple", 4.5)
print(my_tuple[1])  # Accessing an element
```

---

### **Sets**
A set is an unordered collection of unique elements.

#### **Characteristics:**
- Unordered (no specific sequence)
- Mutable (can add or remove elements, but individual elements are immutable)
- Does not allow duplicate elements

#### **Example:**
```python
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Adding an element
print(my_set)
```

---

### **Dictionaries**
A dictionary is an unordered collection of key-value pairs.

#### **Characteristics:**
- Stores data in key-value pairs
- Keys must be unique and immutable (e.g., strings, numbers, tuples)
- Values can be of any data type
- Mutable (can add, remove, or modify key-value pairs)

#### **Example:**
```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_dict["age"] = 26  # Modifying a value
print(my_dict)
```