# Created a Dictionary.
the_dict = {
    
# Brand of car.
"Brand":"Ford",
# Model of car.
"Model":"Endeavour",
# Year of car.
"Year":"2023",
# Year of car.
"Year":"2025",
# Mileage of car.
"Mileage":"10",
# Seates of car.
"Seates":"8",
# Colour of car.
"Colour":"Black",
# Fully Loaded or not.
"Fully Loaded":"Yes"
}
# Type of dictionary.
print(type(the_dict))
# Prinitng of dictionary.
print(the_dict)
# Searching Brand.
print(the_dict["Brand"])
# Searching year.
# Their are duplicate values it will over write;.
print(the_dict["Year"])
# Dictionary length.
print(len(the_dict))
# Another way to get the value.
# Get Method.
x = the_dict.get("Mileage")
print(x)
# It will show me the values.
x = the_dict.values()
# Changing the colour.
print(x)
the_dict["Colour"] = "RED"
# Changes has done, now it will show me the updated items.
x = the_dict.items()
# Using if statement for checking it existing or not.
if "Seates" in the_dict:
    print("Yes, Seates are their in the dictionary.")
# Using if statement for checking it existing or not.
if "Gear" in the_dict:
    print("Yes, it does.")    
else:
    print("No, Please check the item you want to check.")
# Adding items in Dictionary.
the_dict.update({"color": "red"})
# Removing item form the Dictionary.
the_dict.pop("Year")
print(the_dict)
    # Or
# Clearing item from the dictionary.
the_dict.clear()
print(the_dict)
# Using loop for printing the dictionary.
for x, y in the_dict.items():
    print(x, y)
#Copy method you can copy the dictionary
this_dict = the_dict.copy()
print(this_dict)
