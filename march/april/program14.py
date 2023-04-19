#Define a function that accepts roll number and returns whether the student is present or absent.
def detail(roll):
    x = (23,32,43,34)
    if roll in x:
        print("roll number is present")

    else:
        print("roll number is absent")

roll = int(input("enter your roll number:"))
detail(roll)