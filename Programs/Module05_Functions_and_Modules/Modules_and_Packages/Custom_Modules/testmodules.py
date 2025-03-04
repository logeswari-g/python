from banking.accounts import credit, debit, accountinfo

curbalance = credit.initialbal
curbalance = credit.creditbalance(curbalance, 50)
print(curbalance) # 150
curbalance = debit.debitbalance(curbalance, 20)
print(curbalance) # 130

print(accountinfo.bankname) # "HDFC Bank"
print(accountinfo.welcome()) # Welcome to HDFC Bank!

print("******* Class *******")
# Syntax:
# modulename.classname(args)
userobj1 = accountinfo.user("Devid", 1234)
print(userobj1.branch) # Egattur
# accountinfo.branch # AttributeError
print(userobj1.accname) # Devid
print(userobj1.accno) # 1234

name = input("Enter Account Name: ")
number = int(input("Enter Account Number: "))
userobj2 = accountinfo.user(name, number)
print(userobj2.accname) # Arun
print(userobj2.accno) # 5678
print(userobj1.accname) # Devid
print(userobj1.accno) # 1234

print(userobj2.branch)

userobj2.printaccdetails(200)
userobj1.printaccdetails(200)
