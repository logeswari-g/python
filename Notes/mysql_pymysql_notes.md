
# 📝 Notes: Connecting to MySQL using PyMySQL in Python

---

## 📦 1. Install PyMySQL

```bash
pip install pymysql
```

---

## 🔗 2. Connect to MySQL Database

```python
import pymysql

connection = pymysql.connect(
    host='127.0.0.1',       # or 'localhost'
    user='root',            # your MySQL username
    password='your_password',  # your MySQL password
    database='your_db_name',   # database to connect to
    port=3306,              # default MySQL port
    connect_timeout=5
)
```

---

## 🧑‍💻 3. Create Cursor and Execute Queries

```python
cursor = connection.cursor()

# SELECT
cursor.execute("SELECT * FROM student_details")
results = cursor.fetchall()
for row in results:
    print(row)

# INSERT
cursor.execute(
    "INSERT INTO student_details (id, name, coursename, mobilenumber) VALUES (%s, %s, %s, %s)",
    (1, 'John', 'Python', 9876543210)
)
connection.commit()
```

---

## 📋 4. Fetch Methods

| Method          | Description                                |
|-----------------|--------------------------------------------|
| `fetchone()`    | Fetches the next row                       |
| `fetchmany(n)`  | Fetches the next `n` rows                  |
| `fetchall()`    | Fetches all remaining rows                 |

---

## 🧠 5. Use DictCursor to Fetch as Dictionary

```python
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='scrapy_db',
    cursorclass=pymysql.cursors.DictCursor  # Enables dict-style results
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM student_details")
row = cursor.fetchone()
print(row['name'], row['coursename'])
```

---

## ❌ 6. Exception Handling

```python
try:
    connection = pymysql.connect(...)
    print("✅ Connected to DB")
except pymysql.MySQLError as e:
    print(f"❌ Connection Error: {e}")
```

---

## 🔚 7. Close Connection

```python
if connection and connection.open:
    connection.close()
    print("🔌 Connection closed")
```

---