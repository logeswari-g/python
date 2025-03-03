# Variables and Assignments

number = 100 # Integer
score = 90.56 # float
text = "Apple" # String

# Basic Data Types (int, float, str, bool)
flag = "True" # String
flag = True # Boolean

if flag:
    print("Condition satisfied")

# Type Conversion and Casting
# Syntax => type(variableName)

# String to Integer conversion
stringCount = "50" # String
print(type(stringCount))
print(stringCount) # 50 - String
intCount = int(stringCount) # Original variable value will not be changed
print(type(intCount))
print(intCount) # 50 - Integer

# Integer to String conversion
intNum = 1234
print(type(intNum))
print(intNum)
stringNum = str(intNum)
print(type(stringNum))
print(stringNum)
