from Exceptions import InsufficientFunds
#Class is a template for how something is constructed

class Account:
    numCreated = 0

    def __init__(self, initial):
        self._balance = initial
        Account.numCreated += 1

    def deposit(self, amt):
        self._balance += amt
        return

    # def withdraw(self, amt):
    #     if amt <= self._balance:
    #         self._balance -= amt
    #     else:
    #         Exception(print("You have insufficient funds to complete this transaction."))
    #     return self._balance

    def withdraw(self, amt):
        if amt <= self._balance:
            self._balance -= amt
        else:
            raise InsufficientFunds
        return self._balance

    def getbalance(self):
        return self._balance

    def __str__(self):
        return "Account has balance" + str(self.getbalance())

    def __add__(self, other):
        return self.getbalance() + other.getbalance()

    def get_holder_name(self):
        return self.__holder_name

    def set_holder_name(self, name):
        self.__holder_name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description







