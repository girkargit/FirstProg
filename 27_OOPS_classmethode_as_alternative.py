class Employee:
    no_of_leave = 10
    def __init__(self, aname, asalary, arole): # constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}. role is {self.role}"
    @classmethod
    def change_leaves(cls, new_leave):
        cls.no_of_leave = new_leave

    @classmethod # alternative methode
    def from_dash(cls, string):
        # param = string.split("-")
        # return cls(param[0], param[1], param[2])
        return cls(*string.split("-"))

    @staticmethod #
    def printgood(string):
        print("this is good " + string)


abhi = Employee("abhi", 50000, "instructor")
rohan = Employee("rohan", 60000, "Coder")
suraj = Employee.from_dash("suraj-100000-manager")
print(suraj.salary)
print(suraj.printdetails())
print(abhi.printgood("boy"))
print(Employee.printgood("suaraj"))
