class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = "%s.%s@codewithharry.com" %(fname,lname)

    def explain(self):
        return "%s %s." %(self.fname,self.lname)

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"
        return "%s.%s@codewithharry.com" %(self.fname,self.lname)

    @email.setter
    def email(self, str):
        print("Setting now..")
        name = str.split("@")[0]
        self.fname,self.lname = name.split(".")

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

amol = Employee("Amol","kadam")
# suraj = Employee("suraj", "Pasthe")

print(amol.explain())
print(amol.email)
amol.fname = "Amol$$"
print(amol.email)
amol.email = "this.that@codewithharry.com"
print(amol.fname)
print(amol.email)

del amol.email
print(amol.email)