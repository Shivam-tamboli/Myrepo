# write a programe to the swape two numbers without using third number
#a = int(input("please enter the first for a:"))
#b = int(input("please enter the second for b:"))
#a = a+b
#b = a-b
#a = b-a
#print("after the swapping")
#print("the value of a is:",a)
#print(("the value of b is:",b))



#we have another method to swap variable without using third variable
a = int(input("enter the value for a:"))
b = int(input("enter the value for b:"))

a,b=b,a
print("after swapping the numbers:")
print("the value of a is",a)
print("the value of b is",b)