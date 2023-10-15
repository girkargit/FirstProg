# def name(a,b,c,d):
#     print(a,b,c,d)
# name("abhi","amol","omii","suraj")

def funergs(normal, *abhi, **test): # Goes in tupple format
    print(normal)
    for item in abhi:
        print(item , end = ",")
    print("\n------------------------")
    for i , v in test.items():
        print(i , v)
lst = ["abhi","amol","omii","suraj","bhor"] # We can add multiple element in the list.
string = "Hello Good Morning."
kw = {"abhi": "swimmer", "amol":"programmer"}
funergs(string, *lst, **kw)