#python comprehensions

#In python comprehension we have list comprehensoins

ls = []
for i in range (100):
    if i%3 == 0:
        ls.append(i)
print(ls)

# list comperhension

ls = [i for i in range(100) if i%3 == 0 ]
print(ls)

#Dictionary comperhension
dict1 = {i: f"item {i}" for i in range(10) if i%1 == 0}
print(dict1)
#i can reverse the dictionary 
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"/n" ,dict2)


#set comprehension 
dressess = {dress for dress in["dress1","dress2"]}
print(type(dressess))


#Generator comperhension 

evens = (i for i in range(100) if i%2 == 0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())