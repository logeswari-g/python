# Syntax
# range(start, end, step) # start and step are optional
print("******** Range with a Num **********")

for num in range(7): # range(7) => [0,1,2,3,4,5,6]
    print(num)

print("******** Range with Start, End **********")

for num in range(2,7): # range(2,7) => [2,3,4,5,6]
    print(num)

print("******** Range with Start, End and Step **********")

for num in range(2,10,2): # range(2,10,2) => [2,4,6,8]
    print(num)
else:
    print("loop ended")
