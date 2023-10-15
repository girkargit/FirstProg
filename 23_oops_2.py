class Employee:
    no_leave = 10
    pass

harry = Employee()
abhi = Employee()
harry.name = "harry"
harry.role = "Instructor"
harry.salary = 50000
print(harry.__dict__)
abhi.name = "abhi"
abhi.role = "Student"
abhi.salary = 30000
abhi.no_leave = 15 # instance variable
print(abhi.__dict__)
print(harry.no_leave , abhi.no_leave , Employee.no_leave)
Employee.no_leave = 20 # Change by class name only
print(harry.no_leave , abhi.no_leave , Employee.no_leave)