## 🐘 PostgreSQL Connection with psycopg2

### Install psycopg2

```bash
pip install psycopg2-binary
```

### Connect to PostgreSQL

```python
import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="your_db_name",
        user="your_username",
        password="your_password"
    )
    print("✅ Connected to PostgreSQL")

except Exception as e:
    print(f"❌ Error: {e}")
```

### Execute Queries

```python
cursor = connection.cursor()

# SELECT
cursor.execute("SELECT * FROM your_table")
rows = cursor.fetchall()
for row in rows:
    print(row)

# INSERT
cursor.execute("INSERT INTO your_table (id, name) VALUES (%s, %s)", (1, 'John'))
connection.commit()
```

### Close Connection

```python
cursor.close()
connection.close()
print("🔌 Connection closed")
```

---

## MongoDB Connection with PyMongo

### Install pymongo

```bash
pip install pymongo
```

### 🔗 Connect to MongoDB

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["students"]
print("✅ Connected to MongoDB")
```

### Insert Documents

```python
# Single document
collection.insert_one({"name": "Alice", "course": "Python"})

# Multiple documents
collection.insert_many([
    {"name": "Bob", "course": "Java"},
    {"name": "Charlie", "course": "C++"}
])
```

### Query Documents

```python
# Find one
student = collection.find_one({"name": "Alice"})
print(student)

# Find all
for student in collection.find():
    print(student)

# Conditional query
for student in collection.find({"course": "Python"}):
    print(student)
```

### Update and Delete

```python
# Update
collection.update_one({"name": "Alice"}, {"$set": {"course": "Go"}})

# Delete
collection.delete_one({"name": "Bob"})
```

### Close MongoDB Connection (Optional)

```python
client.close()
```

---
