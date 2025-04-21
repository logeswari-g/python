import threading
import time

# Simulate sending email
def send_email(user):
    print(f"Sending email to {user}...")
    time.sleep(2)  # Simulate delay (e.g., waiting for server)
    print(f"Email sent to {user}")

if __name__ == "__main__":
    # List of users
    users = ['Alice', 'Bob', 'Charlie']
    
    # Create and start threads
    threads = []
    for user in users:
        thread = threading.Thread(target=send_email, args=(user,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    print("All emails sent.")
