#How to make recursive function of factorial 
def factorial_recursive(n):
    #if value of n is 1 it will return 1.
    if n==1:
        return 1
    #suppose the value of n is 5
    # 5 * factorial_recursive(4)
    #5 * 4  * factorral_recursive(3)
    # 5 * 4 * 3 * factorail_recursive(2)
    else:
        return n * factorial_recursive(n-1)
    
number = int(input("enter the number:"))    
print("factorial using recursive method",factorial_recursive(number)) 
