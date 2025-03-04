# Method 1 - Concatenation using + operator
companyName = "Ednue Technologies"
suffix = "Pvt Ltd"
print (companyName + " " + suffix)

# Method 2 - '%' or C-style String Formatting
# %s for Strings
# %d for integer
# %f for float
name = "Arun" # String
age = 25 # Integer
score = 99.126456 # Float
# print (name+age) # TypeError: can only concatenate str (not "int") to str
print("%s age is %d. He has scored %.2f in HSC."%(name, age, score))

# Method 3 - .format() method
print ("{} age is {}. He has scored {} in HSC.".format(name, age, score))
print ("{0} age is {2}. He has scored {1} in HSC.".format(name, age, score))

{
    "name": "devid",
    "age": "100"
}

# Method 4 - f'string
personName = "Alex"
companyName = "Google"
print("{personName} works in {companyName}") # {personName} works in {companyName}
print(f"{personName} works in {companyName}") # Alex works in Google

waterAmount = 1.5
noOfTimes = 4
totalAmount = waterAmount * noOfTimes
print(f"{personName} works in {companyName}. He drinks {totalAmount} of water per day.")
print(f"{personName} works in {companyName}. He drinks {waterAmount * noOfTimes} of water per day.")
fruits = {
    "apple": 10,
    "orange": 20,
}
print(f'Apple count are {fruits['apple']}')
