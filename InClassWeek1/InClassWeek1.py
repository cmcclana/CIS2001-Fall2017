from SavingsAccount import *
import copy

def try_method(account, method, amount = 0):
    print("Attempting to", method, str(amount))
    try:
        if method == "deposit":
            account.deposit(amount)
        if method == "withdraw":
            account.withdrawl(amount)
        if method == "earn_monthly_interest":
            account.earn_monthly_interest()
    except ValueError as e:
        print("Error -", e)
    print(account)

vaction_fund = SavingsAccount("123", .01)
vaction_fund.set_account_name("Vaction Fund")

try_method(vaction_fund, "deposit", 100)
try_method(vaction_fund, "deposit", -100)

try_method(vaction_fund, "withdraw", 100)
try_method(vaction_fund, "withdraw", 100)
try_method(vaction_fund, "withdraw", -100)

try_method(vaction_fund, "deposit", 100)
for month in range(12):
    try_method(vaction_fund, "earn_monthly_interest")

retirement_fund = SavingsAccount('1234', .01)
retirement_fund = copy.deepcopy(vaction_fund)

retirement_fund.deposit(100)
print(retirement_fund)
vaction_fund.deposit(100)
print(vaction_fund)


