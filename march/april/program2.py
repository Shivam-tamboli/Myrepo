#find the largest number among three number
num1 = int(input("enter the value to find the largest number:"))
num2 = int(input("enter the value to find the largest number:"))
num3 = int(input("enter the value to find the largest number:"))

if(num1>num2 and num1>num3):
    print("the largest number is",num1)

elif(num2>num1 and num2>num3):
    print("the largest number is",num2)

elif(num3>num1 and num3>num2):
    print("the largest number is",num3)

else:
    print("ERROR")