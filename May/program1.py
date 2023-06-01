#how to make fibonnaci series
def fibonnaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonnaci (n-1) + fibonnaci (n-2)

# 0 1 1 2 3 5 8 13     
number = int(input("enter the value:"))
print("the fibonacci series is",fibonnaci(number))