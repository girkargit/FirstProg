# def func1():
#     print("abhilash")
# func2 = func1
# del func1
# func2()

# def funret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = funret(1)
# print(a)

# def fun_new(fun):
#     fun("this")
# fun_new(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec
# @dec1 # decorator short form
def abhi():
    print("abhi is good boy.")
abhi = dec1(abhi)
abhi()