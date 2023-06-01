#multilevel inheritance
# class class1:  
#     <class-suite>   
# class class2(class1):  
#     <class suite>  
# class class3(class2):  
#     <class suite>

class Dad:
    baskatball = 10
    
class Son(Dad):
    dance = 1
    #create a method
    def isdance(self):
     return f"Yes i dance {self.dance} number of times"

class Grandson(Son):
    dance = 5


darry = Dad()
larry = Son()
marry = Grandson()

print(darry.baskatball)

