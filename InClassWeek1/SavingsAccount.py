from Account import *

class SavingsAccount(Account):
    """description of class"""

    def __init__(self, number, apr):
        super().__init__(number)
        self._apr = apr

    def earn_monthly_interest(self):
        self.deposit( self.get_balance() * self._apr / 12 )

