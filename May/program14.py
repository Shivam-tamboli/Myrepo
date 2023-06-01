#oops
#create a class
class Employee:
    no_of_leaves = 12
    pass    #nothing

#create an objects
shivam=Employee()
satyam=Employee()

shivam.name = "shivam"
shivam.salary = 12345
shivam.role = "student"

satyam.name = "satyam"
satyam.salary = 4321
satyam.role = "student"

print(shivam.no_of_leaves)
print(shivam.__dict__)

