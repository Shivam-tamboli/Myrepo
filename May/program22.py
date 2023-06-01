#Public - it can be use anywhere
#Private - we can't use outside the class
#Protacted - only those can be use which derive by this classes
class Employee:
    no_of_leaves = 12
    var = 13
    _protect = 9
    __private = 34

    def __init__(self, name,salary, role ):
        self.name = name
        self.salary = salary
        self.role = role

shivam = Employee("shivam",123456,"instructor")

#print(shivam.__private)

#if i want to use the private 

print(shivam._Employee__private)