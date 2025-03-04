# Dict Comprehension
# Simply a looping + condition
# Used to filter data & convert List => Dictionary

# Dict Comprehension Syntax
# listVar = { keyExpression: valueExpression for itemVar in iterable if condition }
# listVar = { keyExpression: valueExpression for itemVar in iterable }

fruits = {
    "apple": 7,
    "orange": 20,
    "grapes": 10,
    "pineapple": 6,
    "watermelon": 3,
    "kiwi": 25,
}

orderCount = { fruitName: 10 - stockCount for fruitName, stockCount in fruits.items() if stockCount < 10 }
print(orderCount)

# To find the occurrence of elements in a list
# Normal Method
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

occurrence = {}
for value in values:
    if not value in occurrence.keys():
        occurrence[value] = 1
    else:
        occurrence[value] += 1
print("******* Normal Method *********")
print(occurrence)

# Comprehension Method
occurrence = { value: values.count(value) for value in values }
print("******* Dict Comprehension *********")
print(occurrence)
