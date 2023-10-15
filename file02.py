a = 7
def printjoke(str):
    print(f"This is joke {str}")

def printabhi(str):
    return f"Ye string muje de de thakhur {str}"

def add(num, num1):
    return num + num1 + 5
# when import function in another file bellow output will not printed.
# print("$$$$$$" , __name__)/=
if __name__ == '__main__':
    print(printabhi("Abhilash"))
    o = add(1 , 6)
    print(o)

# n = ["abhi", "omii", "suraj" , "amol"]
# for i in n:
#     print(i , end= " ")