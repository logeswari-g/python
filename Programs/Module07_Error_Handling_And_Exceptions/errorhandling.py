number = 100
denominators = [1, 2, 3, 0, 5, "a", 10]
eligibledenominators = []

for denominator in denominators:
    try:
        result = number / denominator
        print(result)
    except ZeroDivisionError as zde:
        print("Denominator should not be zero(0)")
        print(zde)
    except TypeError as te:
        print("Denominator should not be other than integer")
        print(te)
    else:
        eligibledenominators.append(denominator)

print(eligibledenominators)

num1 = 10
while True:
    try:
        num2 = int(input("enter a number: "))
        break
    except:
        print("Please enter a valid number")

sum = num1 + num2
print(sum)

try:
    text = "abc" + "def"
    # text = 10 + "abc"
    print(text)
except TypeError:
    print("Caught an exception - TypeError")
else: # Executes only when there is no exception
    print("Else block executed")
finally: # Always finally block executes
    print("Finally block executed")

flag = False

while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a denominator: "))
        result = a / b
        print(result)
        flag = True
        break
    # except ZeroDivisionError:
    #     print("Zero division error")
    except ValueError:
        print("Value error")
    finally:
        if flag:
            print("Great - Input is perfect")
        else:
            print("Please provide proper input")

# Sample input to test above example
# 10 0 => error
# 10 a => error
# 10 2 => 5
