z = 76 #This a global variable.
# Created a function named by function 45.
def function45 (n):
     #local variale.
    y = 78
    #printing a statement.
    print(n, "My name is shivam.")
  
    global z
    z = z + 65
    print(z,y)



    #printing function with statement.
function45("this is me")
#Printing the value of.
#it will print the global variable value, until we change the value.
print(z)