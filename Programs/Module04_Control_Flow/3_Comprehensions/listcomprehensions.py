# List Comprehension
# Simply a looping + condition
# Used to filter data & convert Dictionary =>  List

values = [
    10,
    10,
    "abc",
    20,
    "def",
    "def",
    "100",
    30,
    "GHI",
    "Xyz"
]

# To filter integer type values from the list
# Normal Method
filteredValues = []
for value in values:
    if type(value) == int:
        filteredValues.append(value)
print("******* Normal Method *********")
print(filteredValues)

# List Comprehension Syntax
# listVar = [ expression for itemVar in iterable if condition ]
# listVar = [ expression for itemVar in iterable ]

# Comprehension Method
filteredValues = [ value for value in values if type(value) == int ]
print("******* List Comprehension *********")
print(filteredValues)

# To filter the fruits less than 10 count
fruits = {
    "apple": 7,
    "orange": 20,
    "grapes": 10,
    "pineapple": 6,
    "watermelon": 3,
    "kiwi": 25,
}

# lowStockFruits = [ fruit[0] for fruit in fruits.items() if fruit[1] < 10 ]
# ["apple", "pineapple", "watermelon"]

# lowStockFruits = [ (fruit[0], fruit[1]) for fruit in fruits.items() if fruit[1] < 10 ]
# [("apple", 7), ("pineapple", 6), ("watermelon", 3)]

lowStockFruits = [ (fruitName, stockCount) for fruitName, stockCount in fruits.items() if stockCount < 10]
print(lowStockFruits) # [ ("apple", 7), ("pineapple", 6), ("watermelon", 3) ]
