class Employee:
    no_of_leaves = 12
    def __init__(self, name,salary, role ):
        self.name = name
        self.salary = salary
        self.role = role
    
#creating method
    def printdetails(self):
        return f"Name is {self.name}. salary is {self.salary}. and  role is {self.role}" 

#create an objects
shivam=Employee("shivam",123456,"instructor")
# satyam=Employee()

# shivam.name = "shivam"
# shivam.salary = 12345
# shivam.role = "student"

# satyam.name = "satyam"
# satyam.salary = 4321
# satyam.role = "student"

print(shivam.salary)



