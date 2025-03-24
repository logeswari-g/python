import time

# Decorator to measure the execution time of a function
def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate execution time
        print(f"Function {func.__name__} executed in {execution_time:.4f} seconds.")
        return result
    return wrapper

# Applying the decorator to a function
@timeit_decorator
def slow_function():
    print("Starting slow function...")
    time.sleep(10)  # Simulate a slow function (sleep for 2 seconds)
    print("Slow function finished!")

@timeit_decorator
def fast_function():
    print("Starting fast function...")
    time.sleep(5)  # Simulate a fast function (sleep for 1 second)
    print("Fast function finished!")

# Calling the decorated functions
slow_function()
fast_function()
