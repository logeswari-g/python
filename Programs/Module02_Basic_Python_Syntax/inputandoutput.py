# Input
name = input("Enter your name: ")
rollNo = input("Enter your roll no: ")

# Output
print(f"My name is {name} and my roll number is {rollNo}")

# To get multiple inputs in single input command
numbers = input("Enter multiple numbers using comma separator: ") # "1,2,3,4,5,6"
print(type(numbers))
commaSeparatedNumbers = numbers.split(",")
print(commaSeparatedNumbers)

# To check type of input
test = input("Enter something: ")
print(type(test))

# Type conversion/casting
score = input("Enter score: ")
print(type(score)) # <class 'str'>
print("My HSC score: " + score)
# print(100 + score) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(100 + int(score)) # 200
