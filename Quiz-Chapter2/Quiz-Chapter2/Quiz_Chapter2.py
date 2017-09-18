from SalariedEmployee import *
from Employee import *
import copy

def Print_Employee(employee):
    print( "ID: ", employee.ID, "Name: ", employee.Name, "Salary: ", employee.GetSalary())
    if employee.Manager is not None:
        print("Manager: ", employee.Manager.Name)

Ali = SalariedEmployee("123", "Ali", None, 5000)
Sohil = Employee("234", "Sohil", Ali, 10.0)
David = Employee("345", "David", Ali, 12.0 )
Celeste = copy.deepcopy(David)
Celeste.Name = "Celeste"
Celeste.ID = "456"
Celeste.Manager.Name = "Ali"


Print_Employee(Ali)
Print_Employee(Sohil)
Print_Employee(David)
Print_Employee(Celeste)


