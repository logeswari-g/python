# Logical operators => not, and, or

value = int(input("Enter a number: "))

if (value >= 40) and (value <= 60):
    print("Entered number is in range")

if (value == 0) or (value == 1):
    print("Entered number is binary")

if not (value == 1):
    print("Entered number is not 1")

# Method 1
if (value >= 40) and (value <= 50):
    print("Given number range is between 40 and 50")
elif (value >= 80) and (value <= 90):
    print("Given number range is between 80 and 90")

# Method 2 - Simplified
if ((value >= 40) and (value <= 50)) or ((value >= 80) and (value <= 90)):
    print("Given number range is between 40 and 50 or 80 and 90")

if not (value >= 40) and (value <= 50):
    print("Given number range is between 40 and 50")
else:
    print("not is failed")
