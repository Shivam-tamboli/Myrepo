#Abstract base class & abstract method
#we have a module in python name is abc
#And abstract method is a decorater also
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod #means every class need to define this method
    def printarea(self):
        return 0

# Now we need to inherit with class shape    
class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
       self.length = 5
       self.breath = 6

    def printarea(self):
      return self.length * self.breath

rect1 = Rectangle()
print(rect1.printarea())