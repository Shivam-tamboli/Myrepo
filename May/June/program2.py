#Raise in python

# a = input("Enter your name:")
# b = input("How much money you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so we are stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")

#expected output
# Enter your name:shivam
# How much money you earn0
#     raise ZeroDivisionError("b is 0 so we are stopping the program")
# ZeroDivisionError: b is 0 so we are stopping the program


#raise with try and exception.
c = input("Enter your name:")
try:
    print(a)

except Exception as e:
    if c == "shivam":
        raise NameError("This name is not allow")
        
        
    print("Exception handeld")

    #expected otuput
#     Enter your name:koustubh
# Exception handeld