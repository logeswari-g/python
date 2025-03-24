import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",  # Default XAMPP MySQL username
  password="",  # Default XAMPP MySQL password
  database="ednue"
)

mycursor1 = mydb.cursor()
mycursor1.execute("INSERT INTO student_details(id, name, coursename, mobilenumber) VALUES (3,'Alex','C++',454545454)")  # Replace with your table name
mydb.commit()

mycursor2 = mydb.cursor()
mycursor2.execute("SELECT * FROM student_details")  # Replace with your table name
myresult = mycursor2.fetchall()

for x in myresult:
  print(x)

mydb.close()
