import threading
import os
import time

def print_numbers(endnum):
    for i in range(endnum):
        print(i)

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    time.sleep(5)

def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))

if __name__ == "__main__":
    # Normal method
    print('Executed by main thread')

    # Create a thread
    thread = threading.Thread(target=print_numbers, args=(1000,))

    # Start the thread
    thread.start()

    # Wait for the thread to finish
    thread.join()

    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of program")
