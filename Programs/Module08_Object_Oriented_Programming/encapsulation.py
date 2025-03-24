class Bank:
    # public data member
    bankName = None

    # protected data member
    _accNumber = None

    # private data member
    __accBal = None

    # constructor
    def __init__(self, bankName, accNumber, accBal):
        # public data member
        self.bankName = bankName
        # protected data member
        self._accNumber = accNumber
        # private data member
        self.__accBal = accBal

    # public member function
    def displayBankName(self):
        # accessing public data member
        print("Bank name: " + self.bankName)

    # protected member function
    def _displayBalance(self):
        # accessing protected data member
        print("Account number: " + self._accNumber)

    # private member function
    def __displayBalance(self):
        # accessing private data member
        print("Account balance: " + str(self.__accBal))

    # public member function
    def accessPrivateMember(self):
        # accessing private data member
        self.__displayBalance()

class Account(Bank):
    # constructor
    def __init__(self, bankName, accNumber, accBal):
        Bank.__init__(self, bankName, accNumber, accBal)

    # public member function
    def displayBankName(self):
        # accessing public data member
        print("Bank name: " + self.bankName)

    # public member function
    def displayBalance(self):
        # accessing public member function
        Bank.accessPrivateMember(self)

# creating object 1 for Account base class
accountObj1 = Account(
    "HDFC",
    "1234",
    1000
)

# accessing public data members
print(accountObj1.bankName)

# accessing protected data members
print(accountObj1._accNumber)

# accessing private data members
# print(accountObj1.__accBal) # AttributeError: 'Account' object has no attribute '__accBal'
# Syntax: objname._ParentClassName__PrivateDataMember
print(accountObj1._Bank__accBal) # 1000

# accessing public members function
accountObj1.displayBalance()

# creating object 2 for Account base class
accountObj2 = Account(
    "ICICI",
    "5678",
    2000
)

print(accountObj2.bankName)
accountObj2.displayBalance()
