from account import Account, InsufficientFundsException
try:
    christelle_account = Account(1000)

    christelle_account.withdraw(10000)

except InsufficientFundsException as err:
    print(err)



