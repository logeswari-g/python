# Syntax:
# def definitionName():
    # statements

# Function will not be executed until it is called
# Grouping a lines of code for a specific feature
# Code can be reused and called wherever required

def greetings():
    print("Welcome to greetings method!")

greetings() # Function calling

####### Return ########

def greetings2():
    # return "Welcome to greetings method!"
    text = "Welcome to greetings2 method!"
    return text

result = greetings2() # "Welcome to greetings2 method!"
print(result)
print(greetings2())
