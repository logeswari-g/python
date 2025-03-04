# Method 1 - Concatenate at end
print("a value is = ", str(10))

# Method 2 - .format() method
print ("{} age is {}. He has scored {} in HSC.".format(name, age, score))
print ("{0} age is {2}. He has scored {1} in HSC.".format(name, age, score))

# Method 3 - f'string
personName = "Alex"
companyName = "Google"
waterAmount = 1.5
noOfTimes = 4
totalAmount = waterAmount * noOfTimes
print(f"{personName} works in {companyName}. He drinks {waterAmount * noOfTimes} of water per day.")

fruits = {
    "apple": 10,
    "orange": 20,
}
print(f'Apple count are {fruits['apple']}')

# Method 4 - Concatenation using + operator
companyName = "Ednue Technologies"
suffix = "Pvt Ltd"
print (companyName + " " + suffix)

# Method 5 - '%' or C-style String Formatting
# %s for Strings
# %d for integer
# %f for float
name = "Arun" # String
age = 25 # Integer
score = 99.126456 # Float
# print (name+age) # TypeError: can only concatenate str (not "int") to str
print("%s age is %d. He has scored %.2f in HSC."%(name, age, score))
