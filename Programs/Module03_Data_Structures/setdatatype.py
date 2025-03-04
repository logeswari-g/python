# Set
newset = {1,2,3,4,5,1,2,6}
print(newset) # {1,2,3,4,5,6}

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print("Set1:", set1)
print("Set2:", set2)

# Set Operations
print("Union:", set1 | set2) # {1, 2, 3, 4, 5, 6, 7}
print("Intersection:", set1 & set2) # {3, 4, 5}
print("Difference (Set1 - Set2):", set1 - set2) # {1, 2}

# Set Methods
newset.add(9)
print(newset) # [1,2,3,4,5,6,9]

mylist = [1,2,3,4,1,2,5]
myuniqueset = set(mylist)
print(myuniqueset) # {1,2,3,4,5}
mylist = list(myuniqueset)
print(mylist) # [1,2,3,4,5]
