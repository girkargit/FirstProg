class Employee:
    no_leave = 10
    def __init__(self, aname, asalary, arole): # constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}. role is {self.role}"

abhi = Employee("abhi", 50000, "instructor")
rohan = Employee("rohan", 60000, "Coder")

print(abhi.name)
print(abhi.printdetails())