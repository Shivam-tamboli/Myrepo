#My list
my_list = ["Java","Python","c","c++","HTML"]
#type function
print(type(my_list))
#len function
print(len(my_list))

#sliceing in list
print(my_list[1:4])
print(my_list[2:4])

#Elements - append
#Befor Append
print("Befor Append:",my_list)
#Appending
my_list.append("Javascript")
#After Appending
print("After Append:",my_list)

my_list1 = ["1","2","3","4","5"]
#Extend
my_list.extend(my_list1)
print(my_list)


#Expected outputs
# <class 'list'>
# 5
# ['Python', 'c', 'c++']
# ['c', 'c++']
# Befor Append: ['Java', 'Python', 'c', 'c++', 'HTML']
# After Append: ['Java', 'Python', 'c', 'c++', 'HTML', 'Javascript']
# ['Java', 'Python', 'c', 'c++', 'HTML', 'Javascript', '1', '2', '3', '4', '5']
