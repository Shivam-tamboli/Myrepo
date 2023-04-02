#calculate the area of triangle
a = float(input("enter the first side:"))
b = float(input("enter the second side:"))
c = float(input("enter the third side:"))

# for semi perimeter
s = (a + b + c)/2

#calculate for area
area = (s*(s-a)*s(s-b)*s(s-c))**0.5
print("the area of triangle is %0.2f", area)