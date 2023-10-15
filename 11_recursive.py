'''
def factorial_iterative(n):
    """
    :param:Integer
    :return: n * n-1 * n-2 * n-3......1
    n! = n * (n-1)!
    """
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac
num = int(input("Enter a number = "))
op = factorial_iterative(num)
print(op)
'''


def factorial_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #print("output is = ",n * factorial_recursive(n -1))
        print(n)
        return n * factorial_recursive(n -1)
'''
5 * factorial_recursive(4)
5 * 4 * factorial_recursive(3)
5 * 4 * 3 * factorial_recursive(2)
5 * 4 * 3 * 2 * 1 = 120
'''
num = int(input("Enter a number = "))
op = factorial_recursive(num)
print(op)

"""
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        print(fibonacci(n-1) + fibonacci(n - 2))
        return fibonacci(n-1) + fibonacci(n - 2)

num = int(input("Enter a number = "))
print("output = ",fibonacci(num))
"""


