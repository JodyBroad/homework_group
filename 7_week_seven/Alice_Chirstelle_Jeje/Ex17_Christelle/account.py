#creating a brand new class, what is the funtionality it should have and what attributes should it have? How will myself and other people go on to use object instances of it.

class InsufficientFundsException(Exception): # exception raised for insufficient funds once withdraw amount deducted from self balance
    pass


class Account:
    numCreated = 0 # keep track of how many bank accounts have been created
    #self is a template for a bank account
    #constructor
    def __init__(self, initial: object) -> object: #define a method, has to be __init__ - implicitly call it
        self._balance = initial # double dunderscore means it's private

        Account.numCreated += 1

    # self is a specific parameter

    # getter - read (input)

    def get_holder_name(self): #way of getting info
        return self.__holder_name #stored privately here

    #setter - write (output)

    def set_holder_name(self, name): #way of setting info
        self.__holder_name = name

    def getbalance(self):
        return self._balance

    def __str__(self):
        return "Account has balance " + str(self.getbalance())

    def __add__(self, other):
        return self.getbalance() + other.getbalance() # allows us to add 2 bank accounts togther overrides inherited function

    def deposit(self, amt): #deposit is a method
        self._balance += amt
        return

    def withdraw(self, amt):
        if amt <= self._balance:
            self._balance -= amt
            print("£", amt, "was withdrawn new balance is £", self._balance)

        else:
            if amt >= self._balance:
                self._balance -= amt
                print("£", amt, "was withdrawn new balance is £", self._balance)
            raise InsufficientFundsException("You have insufficient funds in your account")
            #return self._balance

    @property #decorator - decorating my description method with property - which is a built in function
    def description(self):
        return self._description #wrap the built in property function around the setter

    @description.setter
    def description(self, description):
        self._description = description


# the main trick!
#def main():

    #homer = Account(350)
    #print(homer.getbalance())

#if __name__ == "__main__":
    #main()

#put in if statement and wrap it up in main trick to stop the 350 going into the other file using these functions.

