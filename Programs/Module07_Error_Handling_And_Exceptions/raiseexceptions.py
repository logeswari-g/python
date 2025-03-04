# Syntax:
# raise ExceptionClassName("some message")

# raise ValueError("This is custom error message for ValueError!") # Program by itself will terminate

try:
    raise ValueError("This is custom error message for ValueError!")
    raise NameError("This is custom error message for NameError!") # This line will not execute
except NameError:
    print("Caught an exception - NameError!")
    raise
except ValueError:
    print("Caught an exception - ValueError!")
    raise # Program terminates when I raise exception
