#Class method
#changes of leaves with a function 
class Employee:
    no_of_leaves = 12
    def __init__(self, name,salary, role ):
        self.name = name
        self.salary = salary
        self.role = role
    
    #class method
    #create a function
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

#creating method
    def printdetails(self):
        return f"Name is {self.name}. salary is {self.salary}. and  role is {self.role}" 

#create an objects
shivam=Employee("shivam",123456,"instructor")
##
shivam.change_leaves(68)
print(shivam.no_of_leaves)