# **XPath and CSS Selector Documentation**

XPath and CSS selectors are powerful tools used for navigating and selecting elements in an HTML/XML document, commonly used in web scraping and automation.

---

## **1. What is XPath?**
XPath (XML Path Language) is used to navigate and query XML and HTML documents. It allows selecting elements based on their structure.

### **Basic Syntax:**
```xpath
//tagname[@attribute='value']
```

### **Examples:**
- Select all `<a>` tags:
  ```xpath
  //a
  ```
- Select a specific `<div>` with class `example`:
  ```xpath
  //div[@class='example']
  ```
- Select the first `<p>` inside a `<div>`:
  ```xpath
  //div/p[1]
  ```
- Select an element with a specific text:
  ```xpath
  //h1[text()='Welcome']
  ```

### **XPath Axes (Navigation Methods)**
- **`parent::`** → Select parent node
- **`child::`** → Select child nodes
- **`following-sibling::`** → Select next sibling nodes
- **`preceding-sibling::`** → Select previous sibling nodes

Example:
```xpath
//div[@id='container']/child::p
```

---

## **2. What is a CSS Selector?**
CSS Selectors are used to target elements based on their attributes, classes, and hierarchy in HTML.

### **Basic Syntax:**
```css
tagname[attribute='value']
```

### **Examples:**
- Select all `<p>` tags:
  ```css
  p
  ```
- Select an element by ID:
  ```css
  #element-id
  ```
- Select elements by class:
  ```css
  .example-class
  ```
- Select direct child elements:
  ```css
  div > p
  ```
- Select sibling elements:
  ```css
  div + p
  ```
- Select elements with an attribute:
  ```css
  input[type='text']
  ```

---

## **3. Differences Between XPath and CSS Selectors**
| Feature | XPath | CSS Selector |
|---------|------|-------------|
| Syntax Complexity | More complex | Simpler |
| Works with XML | Yes | No |
| Parent Selection | Yes | No |
| Performance | Slower | Faster |
| Readability | Harder | Easier |

---

## **4. When to Use XPath vs. CSS Selectors?**
- Use **XPath** when dealing with complex XML/HTML structures or when selecting based on text.
- Use **CSS Selectors** for faster and simpler selections when working with HTML.