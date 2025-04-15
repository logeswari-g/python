## Iterable
An **iterable** is any Python object capable of returning its elements one at a time.  
It must implement the **`__iter__()`** method that returns an **iterator**.

### Examples of Iterable:
- Lists, Tuples, Strings, Sets, Dictionaries, etc.

```python
my_list = [10, 20, 30]
for item in my_list:
    print(item)  # list is iterable
```

### Behind the Scenes:
```python
iter_obj = iter(my_list)  # calls my_list.__iter__()
print(next(iter_obj))     # 10
print(next(iter_obj))     # 20
```

---

## Iterator
An **iterator** is an object that represents a stream of data.  
It implements both **`__iter__()`** and **`__next__()`** methods.

- The `__next__()` method returns the next item.
- Raises **`StopIteration`** when no more data is available.

### Creating a Custom Iterator:
```python
class Counter:
    def __init__(self, max_val):
        self.max = max_val
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

counter = Counter(3)
for num in counter:
    print(num)  # Output: 0 1 2
```

---

## Key Differences: Iterable vs Iterator

| Feature         | Iterable                        | Iterator                          |
|----------------|----------------------------------|-----------------------------------|
| Method Needed  | `__iter__()`                     | `__iter__()` and `__next__()`     |
| Returns        | Returns an iterator              | Returns next item in the sequence |
| Example        | list, tuple, str, set, dict      | object from `iter()` or custom    |
| Usage          | Suitable for `for` loops         | Suitable for manual iteration     |

---

## Convert Iterable to Iterator
```python
nums = [1, 2, 3]         # Iterable
it = iter(nums)          # Now an iterator
print(next(it))          # 1
print(next(it))          # 2
```

---
