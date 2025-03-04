# Method 1 => Numbers of Arguments
def addition(num1, num2):
    sum = num1 + num2
    return sum

print("****** Numbers of Arguments ******")
result1 = addition(10, 20)
print(result1)

# Method 2 => Keyword Arguments
def addition(num2, num1): # Position of arguments is changed
    sum = num1 + num2
    return sum

print("****** Keyword Arguments ******")
result2 = addition(num1 = 10, num2 = 20)
print(result2)

# Method 3 => Arbitrary Arguments (*args)
def addition(*nums): # nums = (10, 20, 30, 40)
    value = ""
    for num in nums:
        value += str(num)
    print(value) #10203040

    return sum(nums) # using python built in method - sum()

print("****** Arbitrary Arguments (*args) ******")
result3 = addition(10, 20, 30, 40)
print(result3)
result4 = addition(10, 20, 30, 40, 50)
print(result4)
result5 = addition()
print(result5)

def subtract(*nums2): # nums = (10, 5)
    value2 = nums2[1]
    value1 = nums2[0]
    return value1 - value2

print(subtract(10,5))

# Method 4 => Keyword Arbitrary Arguments (**kwargs)
def laptopCount(**values):
    # values = {
    #     'name1': 'Dell',
    #     'count1': 10,
    #     'name2': 'Apple',
    #     'count2': 20,
    #     'name3': 'Lenovo',
    #     'count3': 30,
    #     'name4': 'Asus',
    #     'count4': 5
    # }
    print(values)
    print(values['name1'])
    # print(values['name5']) # KeyError: 'name5'
    print(values.get('name5'))

print("****** Keyword Arbitrary Arguments (**kwargs) ******")
laptopCount(name1="Dell", count1=10,
            name2="Apple", count2=20,
            name3="Lenovo", count3=30,
            name4="Asus", count4=5
)

# Default Values
def defaultValues(x, y="Ednue"):
    print (x)
    print (y)

defaultValues(x = 10)
defaultValues(x = 20, y="TCS")
defaultValues(20, "TCS")
