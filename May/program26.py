#operator overloading  &  Dunder method

class Employee:
    no_of_leaves = 23

def __init__(self,name,salary,role):
    self.name = "name"
    self.salary = 5678
    self.role = "instructor"

def print_details(self):
    return f"This is a {self.name}. or salary is{self.salary}. and the role is {self.role}"

# Operater overloading
def add (self, other):
    return self.salary + other.salary


def __repr__(self):
    return f"This is a Empolyee{self.name}. or salary is{self.salary}. and the role is {self.role}"

def __str__(self):
    return f"This is a {self.name}. or salary is{self.salary}. and the role is {self.role}"

emp = Employee()
print(str(emp))         