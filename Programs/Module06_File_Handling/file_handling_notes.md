**File Handling:**

**Advantages:**
- Versatile
  - Read
  - Write
  - Append
  - Create
  - Delete
  - Rename
- User Friendly
  - Syntax is not complex
- Platform independent

**Disadvantage:**
- Prone to Error (Without directory/file permissions, file handling will refrain creating/accessing the files)
- File handling slower compared to other languages

**Functions in File Handling:**
- open()
- read()
- write()
- close()
- tell()
- readlines()

**Syntax for file handling:**
- Method1:
  - open(filename, mode)
- Method2:
  - with open (filename, mode) as fileobj

**Type of Modes:**
- r => read
- w => write
- a => append
- r+ => read & write (read a file & append a content)
- w+ => write & read (truncate/create a file & write a content)
- a+ => read & append
- rb => read binary (eg. Image files)
- wb => write binary (eg. Image files)
- ab => append binary (eg. Image files)
