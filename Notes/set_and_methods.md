# **Python Sets - A Comprehensive Guide**

## **1. Introduction to Sets**
A **set** in Python is an **unordered**, **mutable**, and **unindexed** collection that contains **unique elements**.

### **Example:**
```python
set_example = {1, 2, 3, 4, 5}
print(set_example)  # Output: {1, 2, 3, 4, 5}
```

---

## **2. Set Characteristics**
- **Unordered**: Items do not have a fixed position.
- **Mutable**: Can add or remove elements.
- **Unique Elements**: No duplicate values.
- **Unindexed**: Elements cannot be accessed using an index.

---

## **3. Common Set Methods**

| Method | Description | Example |
|--------|-------------|---------|
| `add(element)` | Adds a single element to the set. | `s = {1, 2}; s.add(3); print(s) # {1, 2, 3}` |
| `update(iterable)` | Adds multiple elements from an iterable. | `s = {1}; s.update([2, 3]); print(s) # {1, 2, 3}` |
| `remove(element)` | Removes an element (raises error if not found). | `s = {1, 2, 3}; s.remove(2); print(s) # {1, 3}` |
| `discard(element)` | Removes an element (does not raise error if not found). | `s = {1, 2, 3}; s.discard(4); print(s) # {1, 2, 3}` |
| `pop()` | Removes and returns a random element. | `s = {1, 2, 3}; print(s.pop())` |
| `clear()` | Removes all elements from the set. | `s = {1, 2, 3}; s.clear(); print(s) # set()` |
| `union(set2)` | Returns a new set with elements from both sets. | `s1 = {1, 2}; s2 = {2, 3}; print(s1.union(s2)) # {1, 2, 3}` |
| `intersection(set2)` | Returns a new set with common elements. | `s1 = {1, 2, 3}; s2 = {2, 3, 4}; print(s1.intersection(s2)) # {2, 3}` |
| `difference(set2)` | Returns a new set with elements only in the first set. | `s1 = {1, 2, 3}; s2 = {2, 3}; print(s1.difference(s2)) # {1}` |
| `symmetric_difference(set2)` | Returns elements in either set but not both. | `s1 = {1, 2, 3}; s2 = {2, 3, 4}; print(s1.symmetric_difference(s2)) # {1, 4}` |
| `issubset(set2)` | Checks if the set is a subset of another. | `{1, 2}.issubset({1, 2, 3}) # True` |
| `issuperset(set2)` | Checks if the set is a superset of another. | `{1, 2, 3}.issuperset({1, 2}) # True` |
| `isdisjoint(set2)` | Checks if two sets have no elements in common. | `{1, 2}.isdisjoint({3, 4}) # True` |
| `copy()` | Returns a shallow copy of the set. | `s1 = {1, 2}; s2 = s1.copy(); print(s2) # {1, 2}` |

---

## **4. Set Comprehension**
Python allows **set comprehension** for concise set creation.

### **Example:**
```python
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}
```

---

## **5. Iterating Over Sets**
You can iterate over a set using a `for` loop.

```python
s = {"apple", "banana", "cherry"}
for item in s:
    print(item)
```

---

## **6. Frozen Sets**
A **frozenset** is an **immutable** version of a set. Once created, its elements cannot be modified.

### **Example:**
```python
fs = frozenset([1, 2, 3, 4])
print(fs)  # Output: frozenset({1, 2, 3, 4})
```

---

## **7. Sample Program**
Below is a sample Python program demonstrating various set methods:

```python
# Sample program demonstrating set methods
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Add and update elements
set1.add(5)
set1.update([6, 7])
print("Updated Set1:", set1)

# Remove elements
set1.remove(7)  # Raises error if not found
set1.discard(8)  # No error if not found
print("After remove and discard:", set1)

# Set operations
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Check relationships
print("Is subset:", {1, 2}.issubset(set1))
print("Is superset:", set1.issuperset({1, 2}))
print("Is disjoint:", set1.isdisjoint({10, 11}))

# Copy and clear
set_copy = set1.copy()
print("Copy of set:", set_copy)
set1.clear()
print("After clear:", set1)
```
