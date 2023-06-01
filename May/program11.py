#how to use filter function
#it filter the list in a truw and false

#now i will create a list
list_1 = [1,2,3,4,5,6,7,8,9,10]

#now i will create a function

def is_greater_5(num):
    return num>5

#now i wil create another list
#now i will type cast in a list
gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)