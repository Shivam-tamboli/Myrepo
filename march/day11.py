#calculator
a = float(input("Enter a value for calculation:"))
b = float(input("Enter a value for calculation:"))

print("Press 1 for addition \n press 2 for subtraction \n press 3 for multiplicatoin \n press 4 for division \n")

choice = int(input("enter your choice  1 to 4 for calculation:"))

if choice == 1 :
    print(a+b)
elif choice == 2 :
    print(a-b)
elif choice == 3 :
    print(a*b)
elif choice == 4 :
    print(a/b)
else :
    print("invalid input")
