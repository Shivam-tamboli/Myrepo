
# class Base1:  
#     <class-suite>  
  
# class Base2:  
#     <class-suite>  
# .  
# .  
# .  
# class BaseN:  
#     <class-suite>  
  
# class Derived(Base1, Base2, ...... BaseN):  
#     <class-suite>  #multiple inheritance 
class Employee:
    no_of_leaves = 12

    def __init__(self,name ,salary ,role):
     self.name = name
     self.salary = salary
     self.role = role

    def print_details(self):
        return f"this is a {self.name}. salary is {self.salary}. and he is a {self.role}"

class Player:
   no_of_games = 5
   def __init__(self, name, game):
      self.name = name
      self.game = game

def printdetaisl(self):
   return f"The name is  {self.name}. game is {self.game}"

class Coolprogrammer(Employee, Player):
   pass

shivam = Employee("Shivam",1234,"instructor")
stayam = Employee("Satyam",1234,"student")

shubham = Player("shubham",["crickert"])
karan = Coolprogrammer("karan", 1234567,"coolprogrammer")

det = karan.print_details()
print(det)