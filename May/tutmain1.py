#using if __name__==__main__
def printfunction(string):
    return f"this is a  {string}"

def add(num1, num2):
    return num1 + num2 + 5

#testing the functions
#if we will use this functoin it will not execute in the file where i will import
print("and the name is ",__name__) 
if __name__ == '__main__':

  print(printfunction("shivam"))
  o = add(3, 5)
  print(o)