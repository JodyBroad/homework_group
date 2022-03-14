class InsufficientFunds(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "InsufficientFundsError, {0}".format(self.message)
        else:
            return "InsufficientFundsError has been raised"


