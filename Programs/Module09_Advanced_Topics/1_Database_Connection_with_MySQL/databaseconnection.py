import pymysql

try:
    print("Connecting using PyMySQL...")

    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='ednue',
        port=3306,
        connect_timeout=5,
        cursorclass=pymysql.cursors.DictCursor
    )

    print("Connected to DB!")

    with connection.cursor() as cursor:
        # cursor.execute("INSERT INTO student_details (id, name, coursename, mobilenumber) VALUES (%s, %s, %s, %s)", (8, 'Pavi', 'Python', 999999999))
        # connection.commit()

        cursor.execute("select * from student_details where coursename = %s", ('Python'))
        results = cursor.fetchmany(4)

        print(f"Data from student_details: {results}")
        # print(results)

except pymysql.MySQLError as e:
    print(f"PyMySQL Error: {e}")

finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Connection closed.")
