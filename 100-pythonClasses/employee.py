class Employee:

    numOfEmp = 0
    raiseAmount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.numOfEmp += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)

print(Employee.numOfEmp)

emp1 = Employee("Corey", "Schefer", 60000)

print(Employee.numOfEmp)

print(emp1.first)
print(emp1.fullname())

emp1.applyRaise()

print(emp1.__dict__)
print(Employee.__dict__)

