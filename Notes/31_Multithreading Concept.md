# Multithreading

## What is Multithreading?
 
In Python, multithreading lets you do multiple things at once — especially useful when some tasks are slow because they are "waiting" (like for a website to respond, a file to load, or a download to finish).

---

## Real Use Case: Sending Emails to Multiple Users

Let’s say you're sending confirmation emails to users after they sign up. Sending emails one by one can be slow — but if you use threads, you can send them **at the same time**.

```python
import threading
import time

# Simulate sending email
def send_email(user):
    print(f"Sending email to {user}...")
    time.sleep(2)  # Simulate delay (e.g., waiting for server)
    print(f"Email sent to {user}")

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
```

### 🧾 Output:
```
Sending email to Alice...
Sending email to Bob...
Sending email to Charlie...
Email sent to Alice
Email sent to Bob
Email sent to Charlie
All emails sent.
```

> Without threading, it would take **6 seconds (2+2+2)**.  
> With threading, it takes **only 2 seconds** (they run at the same time)!


Use multithreading when your program spends time waiting for something — like:

1) Reading/writing files
2) Downloading from the internet
3) Calling APIs
4) Waiting for database queries
5) Sending emails or SMS

Threads can do other work while waiting, making things faster overall.
---
