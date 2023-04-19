#  how to make functon
#def function1(a, b):
#    print("hello you are in function1",a+b)

#function1(5, 7)

def function2(a, b):
    average = (a+b)/2
    print(average)
    
function2(5, 7)

#if you want to store a function in an variable
def function2(a, b):
    """This is a function which will calculate the average of two number"""   #docstring
    average = (a+b)/2
    print(average)
    return average
 
#v = function2(5, 7)
#print (v)

print(function2.__doc__)
