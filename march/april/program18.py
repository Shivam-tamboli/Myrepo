#local and global variable

l = 10  #it is a gloal vraiable

def function1(n):
    l = 5
    m = 8
    global l 
    l = l + 50
    print(l,m)
    print(n,"i have printed")

function1("this is me")

#how to change local intoglobal variable #global keyword
