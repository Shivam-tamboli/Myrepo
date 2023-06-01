#how to use reduce function
from functools import reduce
list1 = [1,2,3,4]
num = 0
for i in list1:
 num = num + i
print(num)

#or we can use reduce function

list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1 )
print(num)