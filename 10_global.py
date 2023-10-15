l = 10 # Global variable
def func(n):
    # l = 5 # local varibale
    # print(l)
    global l # we can change the value of global variable
    l = l + 5
    print(l)
    print(n, "Hii")
func("hellow")
print(l)

def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("Before calling rohan ()" , x)
    rohan()
    print("After calling rohan()" , x)
harry()
print(x)
