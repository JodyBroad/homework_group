from account import Account

# CurrentAccount is a kind of Account
# CurrentAccount is a derived class (subclass)
# Account is a base class (superclass)

# key difference for this one is we want the ability to go overdrawn


class CurrentAccount(Account):

    def __init__(self, initial, overdraft):
        super().__init__(initial)
        self._overdraft = overdraft

    def __str__(self):
        return "Current Account balance is: " + str(self.getbalance())
