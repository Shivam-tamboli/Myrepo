#Define a function that accepts a number and returns whether the number is even or odd.
def func(x):
    if x % 2 == 0:
        print(f"{x} is Even number")
    else:
        print(f"{x} is Odd number")
x = int(input("Enter a number "))
func(x)

#ERROR