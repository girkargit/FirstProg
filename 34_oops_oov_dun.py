class Empolyee:
    no_of_leave = 10
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def prindetails(self):
        print("Name is %s. salary is %s. Role is %s" %(self.name, self.salary, self.role))

    @classmethod
    def change_leaves(cls, newleave):
        cls.no_of_leave = newleave

    def __add__(self, other): # Dunder method and help to add operator over loading.
        return self.salary + other.salary

    def __truediv__(self, other): # Search on mapping operator to function
        return self.salary / other.salary

    def __repr__(self):
        return "Employee('%s', %s, '%s')" %(self.name, self.salary, self.role)

    def __str__(self):
        return "Name is %s. salary is %s. Role is %s" %(self.name, self.salary, self.role)

emp1 = Empolyee("Harry", 400, "programmer")
emp2 = Empolyee("Larry" , 350, "tester")
print(emp1 + emp2)
print(emp1 / emp2)
print(emp1)
print(repr(emp1))
print(str(emp1))