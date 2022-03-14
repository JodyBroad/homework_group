from account import Account
from Exceptions import InsufficientFunds

new_account1 = Account(100)
new_account2 = Account(1000)

new_account1.withdraw(500)
new_account2.withdraw(50)
print(new_account2.getbalance())