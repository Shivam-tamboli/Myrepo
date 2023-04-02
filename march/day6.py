# how to make a faulty calculator , 56 * 3 = 100 , 99 + 1 = 200 , 45 - 2 = 23 
a = float(input("enter a number:"))
b = float(input("entre a number:"))

print("\n press 1 for addition \n press 2 for subtractoin \n press 3 for multipliction \n press 4 for division \n")

choice = int(input("enter your choice 1 to 4 for calculation:"))

if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice == 4:
    print(a/b)
elif choice == 56 * 3:
    print(100)
elif choice == 99 + 1:
    print(200)
elif choice == 45 - 2:
    print(23)
else:
    print("ERROR")
