import random
def computer():
    lst = ["snake" , "water" , "gun"]
    choice = random.choice(lst)
    return choice

user = []
comp = []
tye = []
i = 1
print("Enter game option -> snake , gun , water\nAnd compition between computer and  you.")
while i < 6:
    user_inp = input("Enter a option = ")
    comp_inp = computer()
    if user_inp == comp_inp:
        tye.append(1)
    elif user_inp == "snake" and comp_inp == "water":
        user.append(1)
    elif user_inp == "water" and comp_inp == "gun":
        user.append(1)
    elif user_inp == "gun" and comp_inp == "snake":
        user.append(1)
    else:
        comp.append(1)
    i = i + 1
print("User score is ",sum(user))
print("comp score is ",sum(comp))
print("tye score is ",sum(tye))



