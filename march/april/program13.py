#functions
#build in functions
#a = 4
#b = 8
#c = a + b
#print(c)


# Define a function that accepts 2 values and return its sum, subtraction and multiplication.

#user define function
def result(a, b):
    sum = a + b
    sub = a + b
    mul = a * b
    print( sum ,sub ,mul)

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
result(a,b)