## Make Class Employee.py with Previous Code
from ClassEmployee import Employee as emp

emp1=emp('Zara',2000)
emp2=emp('Mannni',5000)

emp1.displayEmployee()
emp2.displayEmployee()

##other way

import ClassEmployee as emp
emp1=emp.Employee('Zara',2000)

###
from packages.ClassEmployee import Employee as Deep
Deep1=Deep('Kim',5000)
Deep1.displayEmployee()
