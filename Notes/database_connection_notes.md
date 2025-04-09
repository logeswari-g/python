To establish a Python database connection using XAMPP and MySQL, follow these steps:

### 1) Install the MySQL Connector/Python Library

    pip install mysql-connector-python

### 2. Create a Python Script

    import mysql.connector
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",  # Default XAMPP MySQL username
      password="",  # Default XAMPP MySQL password
      database="your_database_name"  # Replace with your database name
    )
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM your_table_name")  # Replace with your table name
    
    myresult = mycursor.fetchall()
    
    for x in myresult:
      print(x)

### Explanation:
- Import: Import the mysql.connector library.
- Connect: Create a connection object using mysql.connector.connect() with the appropriate host, user, password, and database details.
 - Cursor: Create a cursor object to execute SQL queries.
- Execute: Execute your SQL query using mycursor.execute().
- Fetch: Fetch the results using mycursor.fetchall().
- Print: Iterate through the results and print them.

### Important:
- Replace: Replace your_database_name with the actual name of your database.
- Replace: Replace your_table_name with the actual name of your table.
- Start MySQL: Ensure that the MySQL service is running in XAMPP.
