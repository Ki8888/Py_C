class Employee:
    def __init__(self,Name='None',salary=0):
        self.Name = Name
        self.salary=salary
    def calculateSalary(self, Name, dailywage, weekly):
        salary=dailywage*7*weekly
        

emp1=Employee('Zara',2000)
print(emp1.Name,emp1.salary)

emp1.calculateSalary()
print(emp1.name, emp1.salary)