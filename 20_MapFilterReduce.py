# map
lst = ["1","2","3","4","5"]
num = list(map(int , lst))
print(num)

lst1 = [1,2,3,4,5,6,7,8]
num1 = list(map(lambda x: x**2, lst1))
print(num1)

def square(a):
    return a* a
def cube(a):
    return a*a*a
func = [square , cube]
for i in range(5):
    val = list(map(lambda x:x(i) , func))
    print(val , end = " ")

# Filter Return true value only
lst3 = [1,2,3,4,5,6,7,8]
def greater(a):
    return a > 5
x = list(filter(greater , lst3))
print("\n",x)

#reduce
from functools import reduce
h = [1,2,3,4,5]
n = reduce(lambda x , y : x + y , h)
print(n)





