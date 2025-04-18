## Parsing json using python

The `json` module in Python allows you to **encode (serialize)** Python objects into JSON strings and **decode (deserialize)** JSON strings back into Python objects.

---

## Basic Functions

| Function        | Description                                |
|----------------|--------------------------------------------|
| `json.dump()`  | Write Python object to a file as JSON      |
| `json.dumps()` | Convert Python object to JSON string       |
| `json.load()`  | Read JSON from file and convert to object  |
| `json.loads()` | Parse JSON string and convert to object    |

---

## Examples

### 1. Python to JSON (`dumps`)

```python
import json

data = {"name": "Alice", "age": 25, "is_active": True}
json_str = json.dumps(data)
print(json_str)
```

### Output:

```json
{"name": "Alice", "age": 25, "is_active": true}
```

---

### 2. JSON to Python (`loads`)

```python
json_str = '{"name": "Alice", "age": 25, "is_active": true}'
data = json.loads(json_str)
print(data["name"])
```

---

### 3. Write JSON to File (`dump`)

```python
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

### 4. Read JSON from File (`load`)

```python
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
```

---

## Formatting Options

- `indent=4` → pretty print with indentation  
- `sort_keys=True` → sort dictionary keys  
- `separators=(',', ':')` → compact output

```python
print(json.dumps(data, indent=2, sort_keys=True))
```

---
