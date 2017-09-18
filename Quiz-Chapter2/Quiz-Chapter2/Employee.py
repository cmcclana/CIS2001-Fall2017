class Employee(object):
    """description of class"""

    def __init__(self, ID = '', Name = '', Manager = None, Hourly_Rate = 0.0):
        self.ID = ID
        self.Name = Name
        self.Manager = Manager
        self.Hourly_Rate = Hourly_Rate

    def GetSalary(self):
        return 40 * self.Hourly_Rate




