### Project Overview:
Develop a Personal Finance Manager
application.

### Key Features:
- **Add/Edit/Delete Transactions**
- **Categorize Transactions** (e.g., Income, Expenses)
- **Summary Report** (display total income/expenses)
- **Multithreaded Operations** (for background data processing)
- **Input Validation** (using decorators)
- **Error Handling and Data Validation**

---

### 1. Setting up MySQL Database

You'll need to create a MySQL database and table to store your transactions.

```sql
-- Create the database
CREATE DATABASE financemanager;

-- Switch to the new database
USE financemanager;

-- Create a table to store transactions
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2),
    category VARCHAR(255),
    description TEXT,
    date DATE
);
```

### 2. Install Required Python Libraries

To implement this, you'll need some Python libraries. Install them using pip:

```bash
pip install mysql-connector-python
pip install threading
pip install time
```

### 3. Main Python Code

#### File: `financemanager.py`

```python
import mysql.connector
import threading
import time
from datetime import datetime

# Database Connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="financemanager"
    )

# Decorator for validating user input
def validate_input(func):
    def wrapper(*args, **kwargs):
        if not args or not isinstance(args[0], (int, float)):
            print("Invalid amount. Please enter a number.")
            return
        if args[1] not in ['Income', 'Expense']:
            print("Invalid category. Please choose 'Income' or 'Expense'.")
            return
        return func(*args, **kwargs)
    return wrapper

# Transaction Manager Class
class TransactionManager:
    def __init__(self):
        self.connection = create_connection()
        self.cursor = self.connection.cursor()

    @validate_input
    def add_transaction(self, amount, category, description):
        date = datetime.now().date()
        query = "INSERT INTO transactions (amount, category, description, date) VALUES (%s, %s, %s, %s)"
        values = (amount, category, description, date)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"Transaction added: {category} of {amount} on {date}")

    def edit_transaction(self, transaction_id, new_amount, new_category, new_description):
        query = "UPDATE transactions SET amount = %s, category = %s, description = %s WHERE id = %s"
        values = (new_amount, new_category, new_description, transaction_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"Transaction {transaction_id} updated.")

    def delete_transaction(self, transaction_id):
        query = "DELETE FROM transactions WHERE id = %s"
        values = (transaction_id,)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f"Transaction {transaction_id} deleted.")

    def get_summary_report(self):
        query = "SELECT category, SUM(amount) FROM transactions GROUP BY category"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("\n--- Summary Report ---")
        for category, total in result:
            print(f"{category}: {total}")
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Background Processing using Multithreading
def background_task():
    while True:
        print("Running background data processing...")
        time.sleep(10)  # Simulate background task that runs every 10 seconds

# Main Application
def main():
    manager = TransactionManager()
    
    # Starting background processing in a separate thread
    threading.Thread(target=background_task, daemon=True).start()

    while True:
        print("\n1. Add Transaction")
        print("2. Edit Transaction")
        print("3. Delete Transaction")
        print("4. View Summary Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category (Income/Expense): ")
            description = input("Enter description: ")
            manager.add_transaction(amount, category, description)
        elif choice == '2':
            transaction_id = int(input("Enter transaction ID to edit: "))
            new_amount = float(input("Enter new amount: "))
            new_category = input("Enter new category (Income/Expense): ")
            new_description = input("Enter new description: ")
            manager.edit_transaction(transaction_id, new_amount, new_category, new_description)
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID to delete: "))
            manager.delete_transaction(transaction_id)
        elif choice == '4':
            manager.get_summary_report()
        elif choice == '5':
            manager.close_connection()
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
```

### Key Components of the Code

1. **Database Connection (`create_connection`)**:
   - This function establishes the connection to the MySQL database.

2. **TransactionManager Class**:
   - This class handles all operations related to transactions: adding, editing, deleting, and retrieving summary reports.
   - The `add_transaction` method is decorated with `@validate_input` to ensure the user enters valid data.

3. **Multithreading for Background Tasks**:
   - The `background_task` function runs in the background, simulating a process that runs periodically (e.g., syncing data).
   - This is run in a separate thread using Python's `threading` module.

4. **User Interface**:
   - A simple text-based UI is provided in the `main` function for interacting with the application.

### 4. Running the Project

- **Database Setup**: Ensure that the MySQL database and table are correctly set up.
- **Python Code Execution**: Run the Python script using the command:

```bash
python financemanager.py
```

The application will display a menu with options to add, edit, or delete transactions, as well as view the summary report.

### 5. Future Improvements
- **Graphical User Interface (GUI)**: Implement a GUI using libraries like Tkinter or PyQt5 for a better user experience.
- **Authentication**: Add a login system for users to securely manage their finances.
- **Advanced Features**: Implement advanced features like recurring payments, budgets, and expense categories.
