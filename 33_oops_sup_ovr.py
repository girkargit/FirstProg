'''
class A:
    classvar1 = "I am in variablr in class A"
    def __init__(self):
        self.var1 = "I am insaide A's constructor"
        self.classvar1 = "Instance var in class A"
class B(A):
    classvar1 = "I am in class B."

a = A()
b = B()
print(b.classvar1)
'''
# Constructor override methode
class A:
    classvar1 = "I am in variablr in class A"
    def __init__(self):
        self.var1 = "I am insaide A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "special"
class B(A):
    classvar1 = "I am in class B."
    def __init__(self):
        super().__init__() # to use super class insatnce variable
        self.var1 = "I am insaide B's constructor"
        self.classvar1 = "Instance var in class B"
        self.main_class_var  = super().classvar1 # to use super class varibable.
a = A()
b= B()
print(b.classvar1)
print(b.special, b.var1, b.classvar1)
print(b.main_class_var)
