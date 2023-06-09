#Creating a dictionary and taking input from user.
#bI create a Dictionary. 
my_book = {"Atomics Habits" : "Make Good Habbits", 
           "Red Gear":"It Is A Mouse Pad", 
           "The Creator":"A Sci-Fi Movie", 
           "Mc Donald":"The Burger World"}
#Type function 
print(type(my_book))


print("We Have choices in our dictionary:")
print("1.Atomics Habbits\n2.Red Gear\n3.The Creator\n4.Mc Donald's\n")
choice  = (input("Enter your choices Please:"))

if choice == "Atomics Habits":
    print("It is for good Habits")

elif choice == "Red Gear":
    print("It Is A Mouse Pad")

elif choice == "The creator":
    print("A Sci-Fi Movie")

elif choice == "Mc Donald's":
    print("The Burger World")
    
else:
    print("Please Enter a valid choice")