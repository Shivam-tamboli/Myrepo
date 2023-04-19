#write a programe to print a number from user greater then 100 if it is not greater then 100 so it will ask input again til you enter greater 100
while(True):
    num = int(input("enter the number"))
    if(num>100):
        print("congralutions")
        break
    else:
        continue