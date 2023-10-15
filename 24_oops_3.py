class Employee:
    no_leave = 10
    def printdetails(self):
        return "name is %s. role is %s. salary is %s" %(self.name,self.role,self.salary)
harry = Employee()
abhi = Employee()

harry.name = "harry"
harry.role = "Instructor"
harry.salary = 50000

abhi.name = "abhi"
abhi.role = "Student"
abhi.salary = 30000
abhi.no_leave = 15 #
print(abhi.printdetails())