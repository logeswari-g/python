# **Regular Expressions (Regex) in Python**

Regular Expressions (Regex) are powerful tools used for pattern matching and text processing. Python provides the `re` module to work with regex efficiently.

---

## **2. Importing the `re` Module**
To use regex in Python, first, import the `re` module:
```python
import re
```

---

## **3. Basic Regex Functions in Python**
| Function | Description |
|----------|-------------|
| `re.match()` | Checks if a pattern matches at the **beginning** of a string. |
| `re.search()` | Searches for the **first occurrence** of a pattern anywhere in a string. |
| `re.findall()` | Returns **all occurrences** of a pattern in a string as a list. |
| `re.finditer()` | Returns an iterator with match objects for all occurrences. |
| `re.sub()` | Replaces occurrences of a pattern with a given string. |
| `re.split()` | Splits a string based on a pattern. |

---

## **4. Common Regex Metacharacters**
| Metacharacter | Description |
|--------------|-------------|
| `.` | Matches any character except a newline. |
| `^` | Matches the beginning of a string. |
| `$` | Matches the end of a string. |
| `*` | Matches **0 or more** occurrences of the previous character. |
| `+` | Matches **1 or more** occurrences of the previous character. |
| `?` | Matches **0 or 1** occurrence of the previous character. |
| `{n,m}` | Matches between `n` and `m` occurrences. |
| `[]` | Matches any one character inside the brackets. |
| `|` | Acts as an OR operator (e.g., `a|b` matches 'a' or 'b'). |
| `()` | Groups expressions together. |

---

## **5. Examples of Using Regex in Python**

### **Matching a Pattern in a String**
```python
import re
pattern = r"hello"
text = "hello world"
match = re.match(pattern, text)
if match:
    print("Match found!")
else:
    print("No match")
```

### **Finding All Matches**
```python
import re
pattern = r"\d+"  # Matches one or more digits
text = "There are 42 apples and 56 oranges."
numbers = re.findall(pattern, text)
print(numbers)  # Output: ['42', '56']
```

### **Replacing Text Using `re.sub()`**
```python
import re
pattern = r"apples"
text = "I like apples and apples are tasty."
new_text = re.sub(pattern, "bananas", text)
print(new_text)  # Output: "I like bananas and bananas are tasty."
```

### **Splitting a String Based on a Delimiter**
```python
import re
pattern = r",\s*"
text = "apple, banana, cherry, date"
fruits = re.split(pattern, text)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
```

---

## **6. Using Special Sequences**
| Sequence | Description |
|----------|-------------|
| `\d` | Matches any digit (0-9). |
| `\D` | Matches any non-digit character. |
| `\w` | Matches any word character (letters, digits, underscore). |
| `\W` | Matches any non-word character. |
| `\s` | Matches any whitespace character. |
| `\S` | Matches any non-whitespace character. |

Example:
```python
import re
pattern = r"\d{3}-\d{2}-\d{4}"  # Matches a format like 123-45-6789
text = "My SSN is 123-45-6789."
match = re.search(pattern, text)
print(match.group())  # Output: 123-45-6789
```

---

## **7. Compiling Regular Expressions**
For better performance, compile regex patterns before using them multiple times.
```python
import re
pattern = re.compile(r"\d+")
text = "Price: 100 dollars"
match = pattern.search(text)
print(match.group())  # Output: 100
```

---

## **8. Practical Use Cases of Regex**
- **Validating Emails:**
```python
import re
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))
print(validate_email("test@example.com"))  # Output: True
```

- **Extracting URLs from Text:**
```python
import re
text = "Visit our site at https://example.com or http://test.com"
pattern = r"https?://\S+"
urls = re.findall(pattern, text)
print(urls)  # Output: ['https://example.com', 'http://test.com']
```

- **Checking for Phone Numbers:**
```python
import re
pattern = r"\(\d{3}\) \d{3}-\d{4}"  # Format: (123) 456-7890
text = "Call me at (123) 456-7890."
match = re.search(pattern, text)
print(match.group())  # Output: (123) 456-7890
```

# **Regex Flags: `i`, `g`, `s`**  

## **1. Introduction to Regex Flags**  
Regex (Regular Expressions) are used for pattern matching in text. Flags modify how the regex behaves.  

The three commonly used flags are:  
- **`i` (Ignore Case)** → Makes the pattern case-insensitive.  
- **`g` (Global Search)** → Finds all matches instead of stopping at the first one.  
- **`s` (Dotall Mode)** → Allows `.` to match newline characters (`\n`).  

---

## **2. Explanation of Flags**  

### **1. `i` - Case Insensitive Matching**  
- By default, regex is case-sensitive.  
- The `i` flag makes it match letters in any case.  
- Example:  
  ```javascript
  /hello/i.test("HELLO"); // true
  ```

### **2. `g` - Global Search**  
- By default, regex stops after the first match.  
- The `g` flag ensures it finds all occurrences.  
- Example:  
  ```javascript
  "banana".match(/a/g); // ["a", "a", "a"]
  ```

### **3. `s` - Dotall Mode**  
- Normally, `.` does **not** match newlines (`\n`).  
- The `s` flag allows `.` to match **any** character, including newlines.  
- Example:  
  ```javascript
  /a.b/s.test("a\nb"); // true
  ```

---

## **3. Example Usage in JavaScript**  
```javascript
const text = "Hello\nhello HeLLo";
const regex = /hello/igs; // Case-insensitive, global, dotall mode

console.log(text.match(regex)); // ["Hello", "hello", "HeLLo"]
```

---

| Flag | Description | Example |
|------|------------|---------|
| `i`  | Case-insensitive match | `/hello/i` matches `"HELLO"` |
| `g`  | Global search (find all matches) | `/a/g` finds all `"a"` in `"banana"` |
| `s`  | Dot matches newlines (`\n`) | `/a.b/s` matches `"a\nb"` |

These flags can be combined, for example, `/pattern/igs` for case-insensitive, global, and dotall matching.
---
