# def func_1():
#     print("hii abhilash")
# func_1()

def average(x , y):
    '''This is the func which will give you average.'''
    avg = (x + y) / 2
    return avg # other wise it will give us None value.
print(average.__doc__)
a = average(4 , 6)
print(a)