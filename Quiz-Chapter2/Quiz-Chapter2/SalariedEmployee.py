from Employee import *

class SalariedEmployee(Employee):
    """description of class"""

    def __init__(self, ID = '', Name = '', Manager = None, Weekly_Salary = 0):
        super().__init__(ID, Name, Manager)
        self.Weekly_Salary = Weekly_Salary

    def GetSalary(self):
        return self.Weekly_Salary
