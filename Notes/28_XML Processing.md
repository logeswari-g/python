## What is `ElementTree`?

`xml.etree.ElementTree` is a built-in Python module used for parsing and creating XML data.

It's efficient and easy to use for small to medium-sized XML documents.

---

## How to Import

```python
import xml.etree.ElementTree as ET
```
---

## Parsing from String

```python
import xml.etree.ElementTree as ET

xml_data = '''<library>
    <book id="101">
        <title>Python Basics</title>
        <author>John Doe</author>
    </book>
    <book id="102">
        <title>Advanced Python</title>
        <author>Jane Smith</author>
    </book>
</library>'''

# Parse the XML string
root = ET.fromstring(xml_data)

# Root tag
print(root.tag)  # Output: library
```

---

## Looping Through Elements

```python
for book in root.findall('book'):
    book_id = book.get('id')
    title = book.find('title').text
    author = book.find('author').text
    print(f"Book ID: {book_id}, Title: {title}, Author: {author}")
```

**Output:**
```
Book ID: 101, Title: Python Basics, Author: John Doe
Book ID: 102, Title: Advanced Python, Author: Jane Smith
```

---

## Parsing from XML File

If you have an XML file like `library.xml`:

```python
tree = ET.parse('library.xml')
root = tree.getroot()

for book in root.findall('book'):
    print(book.find('title').text)
```
---
