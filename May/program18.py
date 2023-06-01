#static method
class Employee:
    pass

shivam = Employee()
shivam.name = "Shivam"
shivam.roll = "instructor"
shivam.salary = 50000
print(shivam.name)


#static method using with f string
@staticmethod
def print_name(string):
    print("this is a " + string)

print(print_name("shivam"))
