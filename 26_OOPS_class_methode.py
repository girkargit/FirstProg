class Employee:
    no_of_leave = 10
    def __init__(self, aname, asalary, arole): # constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}. role is {self.role}"

    @classmethod # to access instance
    def change_leaves(cls, new_leave):
        cls.no_of_leave = new_leave

abhi = Employee("abhi", 50000, "instructor")
rohan = Employee("rohan", 60000, "Coder")

print(abhi.no_of_leave)
Employee.change_leaves(20)
print(Employee.no_of_leave)
print(abhi.no_of_leave)