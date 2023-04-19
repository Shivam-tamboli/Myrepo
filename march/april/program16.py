#try exception handling
#print("enter the value of a:")
#a  = (input())
#print("enter the value of b")
#b = (input())
#print("the sum of a and b is",int(a)+int(b))

#what if i give second input as a string 
print("enter the value of a:")
a  = (input())
print("enter the value of b")
b = (input())
try:
    print("the sum of a and b is",int(a)+int(b))

except Exception as e:
    print(e)

print("this line is important")

