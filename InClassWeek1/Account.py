class Account(object):
    """description of class"""

    def __init__(self, number):
        self._name = ''
        self._number = number
        self._balance = 0

    def set_account_name(self, name):
        self._name = name

    def get_account_name(self):
        return self._name

    def get_account_number(self):
        return self._number

    def get_balance(self):
        return self._balance

    # Precondition - must have positive balance
    # Postcondition - balance decreased amount, if 0 < amount < balance
    def withdrawl(self, amount):
        if self._balance < amount:
           raise ValueError("Insufficent Balance")
        elif amount < 0:
            raise ValueError("Can't withdraw negative dollars")
        else:
            self._balance -= amount

    # precondition - None
    # postconidition - Balance increased by amount
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Can't deposit negative dollars")
        else:
            self._balance += amount

    def __str__(self):
        return "Account Name: " + self._name + " - Number: " + str(self._number) + " - Balance: " + str(self._balance)

