## **1. Introduction to Dictionaries**
A **dictionary** in Python is an **unordered**, **mutable**, and **indexed** collection that stores data in **key-value pairs**.

### **Example:**
```python
dict_example = {"name": "Alice", "age": 25, "city": "New York"}
print(dict_example)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

---

## **2. Dictionary Characteristics**
- **Unordered**: Items have no fixed position.
- **Mutable**: Can be modified (add, remove, update values).
- **Indexed by Keys**: Access elements using unique keys.
- **Duplicate Keys Not Allowed**: Each key must be unique.

---

## **3. Common Dictionary Methods**

| Method      | Description | Example |
|------------|-------------|---------|
| `keys()` | Returns a view object of dictionary keys | `dict_example.keys()` |
| `values()` | Returns a view object of dictionary values | `dict_example.values()` |
| `items()` | Returns a view object of dictionary key-value pairs | `dict_example.items()` |
| `get(key, default)` | Returns value for key, or default if key not found | `dict_example.get("name")` |
| `update(dict2)` | Merges dictionary `dict2` into the existing dictionary | `dict_example.update({"age": 30})` |
| `pop(key)` | Removes the item with the given key and returns its value | `dict_example.pop("city")` |
| `popitem()` | Removes and returns the last inserted key-value pair | `dict_example.popitem()` |
| `setdefault(key, default)` | Returns the value of a key, or inserts key with default if missing | `dict_example.setdefault("country", "USA")` |
| `clear()` | Removes all elements from the dictionary | `dict_example.clear()` |
| `copy()` | Returns a shallow copy of the dictionary | `copy_dict = dict_example.copy()` |

---

## **4. Dictionary Comprehension**
Python allows **dictionary comprehension** for concise dictionary creation.

### **Example:**
```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Filtering Example:
```python
ages = {"Alice": 25, "Bob": 30, "Charlie": 35}
adults = {k: v for k, v in ages.items() if v >= 30}
print(adults)  # Output: {'Bob': 30, 'Charlie': 35}
```

---

## **5. Iterating Over Dictionaries**
You can iterate over a dictionary using a `for` loop.

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## **6. Nested Dictionaries**
Dictionaries can contain other dictionaries, forming **nested dictionaries**.

### **Example:**
```python
students = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "Los Angeles"}
}
print(students["Alice"]["city"])  # Output: New York
```

---

## **7. Sample Program**
Below is a sample Python program demonstrating various dictionary methods:

```python
# Sample program demonstrating dictionary methods
demo_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Get keys and values
print("Keys:", demo_dict.keys())
print("Values:", demo_dict.values())

# Add and update values
demo_dict["country"] = "USA"
demo_dict.update({"age": 26})
print("Updated Dictionary:", demo_dict)

# Remove elements
removed_value = demo_dict.pop("city")
print("After pop:", demo_dict, "Removed Value:", removed_value)

demo_dict.popitem()
print("After popitem:", demo_dict)

# Copy dictionary
copy_dict = demo_dict.copy()
print("Copy of Dictionary:", copy_dict)

# Clear dictionary
demo_dict.clear()
print("After clear:", demo_dict)
```
