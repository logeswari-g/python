## **1. Introduction to Lists**
**list** in Python is a collection of items that are:
- **Ordered**: Elements maintain the order of insertion.
- **Mutable**: Can be modified (add, remove, change elements).
- **Heterogeneous**: Can hold different data types.
- **Allow Duplicates**: Can store repeated values.
- **Indexable**: Elements can be accessed using indexes.

### **Example:**
```python
my_list = [10, "hello", 3.14, True]
print(my_list)  # Output: [10, 'hello', 3.14, True]
```

---

## **2. List Methods**

| Method      | Description | Example |
|------------|-------------|---------|
| `append(x)` | Adds `x` to the end of the list | `fruits.append("cherry")` |
| `extend(iterable)` | Adds multiple elements | `numbers.extend([4, 5, 6])` |
| `insert(i, x)` | Inserts `x` at index `i` | `fruits.insert(1, "mango")` |
| `remove(x)` | Removes first occurrence of `x` | `nums.remove(2)` |
| `pop(i)` | Removes and returns item at index `i` | `popped = nums.pop(1)` |
| `index(x)` | Returns index of first occurrence of `x` | `index = fruits.index("banana")` |
| `count(x)` | Counts occurrences of `x` | `count = nums.count(2)` |
| `sort()` | Sorts list in ascending order | `nums.sort()` |
| `reverse()` | Reverses the list | `nums.reverse()` |
| `copy()` | Returns a shallow copy | `copy_list = original.copy()` |
| `clear()` | Removes all elements | `nums.clear()` |

---

## **3. List Comprehension**
Python allows concise list creation using list comprehension.

### **Example:**
```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

Filtering Example:
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4, 6]
```

---

## **4. Iterating Over Lists**
You can loop through a list using a `for` loop.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Using `enumerate()` to get index and value:
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

---

## **5. Nested Lists**
A list can contain other lists, forming a **nested list**.

### **Example:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Output: 6
```

---

## **6. Sample Program**
Below is a sample Python program demonstrating all the list methods:

```python
# Sample program demonstrating list methods
my_list = [1, 2, 3]

# Append
my_list.append(4)
print("After append:", my_list)  # [1, 2, 3, 4]

# Extend
my_list.extend([5, 6, 7])
print("After extend:", my_list)  # [1, 2, 3, 4, 5, 6, 7]

# Insert
my_list.insert(2, 10)
print("After insert:", my_list)  # [1, 2, 10, 3, 4, 5, 6, 7]

# Remove
my_list.remove(3)
print("After remove:", my_list)  # [1, 2, 10, 4, 5, 6, 7]

# Pop
popped_value = my_list.pop(3)
print("After pop:", my_list, "Popped Value:", popped_value)  # [1, 2, 10, 5, 6, 7], 4

# Index
index = my_list.index(10)
print("Index of 10:", index)  # 2

# Count
count = my_list.count(2)
print("Count of 2:", count)  # 1

# Sort
my_list.sort()
print("After sort:", my_list)  # [1, 2, 5, 6, 7, 10]

# Reverse
my_list.reverse()
print("After reverse:", my_list)  # [10, 7, 6, 5, 2, 1]

# Copy
copy_list = my_list.copy()
print("Copy of list:", copy_list)  # [10, 7, 6, 5, 2, 1]

# Clear
my_list.clear()
print("After clear:", my_list)  # []
```

---
