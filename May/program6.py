# *args 
# it is passes the argument 


#Nowi will make a functions 
#we can change the name of args to anything
def funargs(*args):
    #Now i will use the for loop 
   for items in args:
      print(items)
      
har =  ["shivam","ansh","nishit","harsh","priyanshu"]
print(*har)