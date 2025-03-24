### Multithreading Explanation:

- We define a function print_numbers() that will be executed in the thread.
- We create a Thread object, passing the print_numbers function as the target.
- We call start() to initiate the thread's execution.
- We call join() to wait for the thread to complete before proceeding.
- Finally, we print a message indicating that the thread has finished.
