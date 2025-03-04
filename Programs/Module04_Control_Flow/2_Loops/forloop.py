# Syntax:
# for item_var in range/iterable:
#     statements

# Looping a List
names = [
    "Alex",
    "Arun",
    "Ajay"
]

for name in names:
    print(name, end="-")
print("\n") # Came out of Loop

# Looping a String
companyName = "Ednue"
for letter in companyName:
    print(letter)

# Looping a Dictionary
fruits = {
    "apple": 10,
    "grapes": 20,
    "orange": 30,
}

for fruit in fruits:
    print(fruit)

for fruit in fruits.items():
    print(fruit)
    print("key: " + fruit[0])
    print("value :", fruit[1])

# fruits.values() # [10, 20, 30]
for fruit in fruits.values():
    print(fruit)

keyslist = fruits.keys()
print(keyslist)

# 1 fruit = ("apple", 10)
# 2 ("grapes", 20)
# 3 ("orange", 30)

for fruit in fruits:
    print(fruit)

fruit = ("apple", 10)
# Using items dictionary method (Method 1)
for fruit in fruits.items():
    print("Key is " + fruit[0])
    print("Value is " + str(fruit[1]))

# Using items dictionary method (Method 2)
for (key, value) in fruits.items():
    print(f"Count of {key} is {value}")

# Using dictionary method - keys() & values
fruitKeys = fruits.keys() # ["apple", "grapes", "orange"]
print(fruitKeys)

total = 0
for count in fruits.values():
    total += count # total = total + count
print("Sum of fruits " + str(total))
