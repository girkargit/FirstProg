# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod
class Shape(ABC): # can not create object of abstract class
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    side = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def printarea(self):
        return self.length * self.breadth

rec = Rectangle()
print(rec.printarea())