# Syntax:
# value_if_true if condition else value_if_false

mark = 60
result = "Pass" if (mark > 50) else "Fail"
print("Type 1 ternary operation result: " + result)

# What if I have written above code in normal method
mark = 60
if (mark > 50):
    result = "Pass"
else:
    result = "Fail"
print("Type 1 normal method result : " + result)

###############################################################

# Syntax: Nested ternary operation
# value_if_true if condition else (value_if_true if condition else value_if_false)
# if -> else (if & else)

mark = 60
result = "Fail" if (mark < 50) else "Outstanding" if (mark > 90) else "Average"
print("Type 2 ternary operation result: " + result)

# What if I have written above code in normal method
mark = 60
if (mark < 50):
    result = "Fail"
else:
    if (mark > 90):
        result = "Outstanding"
    else:
        result = "Average"
print("Type 2 normal method result: " + result)
