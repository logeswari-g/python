### What is a Generator?
- A **generator** is a function that returns an iterator using the `yield` keyword instead of `return`.
- It yields one value at a time and saves the execution state between calls.
- Useful for memory-efficient processing of large data.

### Example: Number Generator
```python
def number_generator():
    for i in range(5):
        yield i

for num in number_generator():
    print(num)
```
**Output:**
```
0
1
2
3
4
```

### Real-time Use Case: Reading Large Files Line by Line
```python
def read_large_file(filepath):
    with open(filepath) as file:
        for line in file:
            yield line
```
- Efficient for processing logs or large datasets without loading the entire file into memory.

---

### What is a Decorator?
- A **decorator** is a function that wraps another function to extend its behavior without modifying the original function.
- Common use cases: logging, timing, authorization, memoization, etc.

### Basic Example
```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```
**Output:**
```
Something before the function runs.
Hello!
Something after the function runs.
```

### Real-time Use Case: Logging Decorator
```python
import time

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} completed in {end - start:.2f}s")
        return result
    return wrapper

@logger
def process_data():
    time.sleep(2)
    print("Processing complete")

process_data()
```
- Helps in tracking function execution time in real-world apps.

---
