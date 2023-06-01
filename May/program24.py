#Method overriding 
class A:
    classvar1 = "I am a class variable in class A"
  #creating a constructor
    def __init__(self):
        self.var1 = "I am inside class A's construcor"
        self.classvar1 = "instance variable in class A" 
        self.special = "Special" 

#Now i will make another class and i will inherite with class A
class B(A):
   classvar1 = "I am in class B"    
# Now i made  constructor  to override
   def __init__(self):
        # class A's constuctor will also work
        super().__init__()


        self.var1 = "I am inside class B's construcor"
        self.classvar1 = "instance variable in class B" 
        print(super().classvar1)  #class A's

a = A()
b = B()

#print(b.classvar1) #first he will find out the instance variable
print(b.special)
