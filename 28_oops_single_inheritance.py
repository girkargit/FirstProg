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

class Programmer(Employee):
    no_holidays = 12
    def __init__(self, aname, asalary, arole, alanguage):  # constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage

    def printprog(self):
        return f"The programmer details  = name is {self.name}. salary is {self.salary}. role is {self.role}. Languge are {self.language}"

abhi = Employee("abhi", 50000, "instructor")
rohan = Employee("rohan", 60000, "Coder")
suraj = Programmer("suraj", 200000, "programmer", ["python"])
omii = Programmer("omkar" , 500000, "AI", ["python"])

print(omii.printprog() , omii.printgood("hii"))
print(omii.no_holidays, omii.no_of_leave)
print(omii.printprog())


