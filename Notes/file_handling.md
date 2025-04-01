# File Handling in Python

File handling in Python allows users to create, read, update, and delete files. Python provides built-in functions to handle files efficiently.

### **File Modes**
| Mode | Description |
|------|-------------|
| `r`  | Read (default mode) – Opens the file for reading. Error if the file does not exist. |
| `w`  | Write – Opens the file for writing. Creates a new file if it does not exist or truncates the existing file. |
| `a`  | Append – Opens the file for appending data. Creates a new file if it does not exist. |
| `x`  | Exclusive creation – Creates a new file. Fails if the file already exists. |
| `b`  | Binary mode – Used with `rb`, `wb`, etc., for binary files. |
| `t`  | Text mode (default) – Used with `rt`, `wt`, etc., for text files. |

### **Files Handling Methods**
- `read(size)`: Reads the specified number of bytes (default: entire file).
- `readline()`: Reads one line at a time.
- `readlines()`: Reads all lines and returns a list.
- `file.write`: Write a content into file.

## **Opening a File**
Python uses the `open()` function to open a file.

**Method 1**
```python
file = open("filename", "mode")
```

**Method 2**
```python
with open("example.txt", "r") as file:
```

## **Reading a File**
```python
with open("example.txt", "r") as file:
    content = file.read()
```

### **Example:**
```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## **Writing to a File**
```python
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
```

## **Appending to a File**
```python
with open("example.txt", "a") as file:
    file.write("\nAppending new content.")
```
- Adds data to the end of the file.

## **Working with Binary Files**
```python
with open("image.jpg", "rb") as file:
    binary_data = file.read()
```

## **Deleting a File**
```python
    os.remove("example.txt")
```
