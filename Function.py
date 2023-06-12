#create a function 
def add (a, b):
    #This function is used for Adding two numbers.
    return a + b

def sub (a, b):
     #This function is used for Subtracting two numbers.
    return a - b

def mul (a, b) :
    # #This function is used for Multiplying two numbers.
    return a * b

def div (a, b):
    # #This function is used for Divison two numbers.
    return a / b

#Asking choice from the user.

print("Please enter your choice:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Please enter your choice:"))

num1 = int(input("Please  enter a number:"))
num2 = int(input("Please enter a number:  "))


if choice == 1:
    print( num1, "+" ,num2,"=" ,add (num1,num2))


elif choice == 2:
    print(num1, "-" ,num2,"="  ,sub(num1,num2))


elif choice == 3:
    print(num1, "*" ,num2, "="  ,mul(num1,num2))


elif choice == 4:
    print(num1, "/" ,num2, "=" ,div(num1,num2))

else :
    print("Choose a valid option")

