#create a function.
#Two arguments.
def function (a, b):
   #This function multiplys the a * b.
   mul = a * b
   #It returns mul means multiply.
   return mul

#We are using try.
#As we can see the second argument is a string not a integer.
#But i want to run my program.
try:
    print(function(12, y))
#Now it will run.
except Exception as e:
    print("This line are very precious for this program")