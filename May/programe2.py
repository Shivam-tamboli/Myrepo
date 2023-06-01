#How to make factorial with itetrative approch
def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
        return fac
    
number = int(input("Enter the value :"))
print("factorial with iterative approch", factorial (number))