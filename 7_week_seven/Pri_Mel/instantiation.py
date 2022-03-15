import sys

from account import Account, InsufficientFundsException

lisa_account = Account(1000)
lisa_account.deposit(200)
print("Lisa's balance is", lisa_account.getbalance())

# bart_account = Account(50)
# print("Bart's balance is", bart_account.getbalance())

try:
    lisa_account.withdraw(1201)
       # bart_account.deposit(75)
except InsufficientFundsException as err:
    print(err, file=sys.stderr)

print("Lisa's balance is", lisa_account.getbalance())
# print("Bart's balance is", bart_account.getbalance())

print(lisa_account)
# print(bart_account)

# total_balance = lisa_account.getbalance() + bart_account.getbalance()
# print(total_balance)

# total_balance2 = lisa_account + bart_account
# print(total_balance2)