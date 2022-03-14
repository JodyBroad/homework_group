# from account import Account
# from savings_account import SavingAccount
# from current_account import CurrentAccount

class InsufficientFundsException(Exception):
    # raised when customer tries to withdraw more money than they have in the account
    # def __init__(self, *args):
    #     if not all(*args):
    #         raise InsufficientFundsException('You have insufficient funds for this withdrawal')
    #
    def __str__(self):
        self.message = ("You do not have enough money to make that withdrawal")
        return self.message

    # def __init__(self, *args):
    #     if args:
    #         self.message = args[0]
    #     else:
    #         self.message = None

    # def __str__(self):
    #     if self.message:
    #         return 'InsufficientFundsException, {0}'.format(self.message)
    #     else:
    #         return 'You have insufficient funds for this transaction'

# raise InsufficientFundsException("You have insufficient funds for this transaction")
