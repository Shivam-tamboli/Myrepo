# for loop
#list1 = ["harry","carry","larry","marry"]
#for items in list1:
#    print(items)

list3 = [["harry",1],["carry",2],["larry",1],["marry",1]]
for items,lollypops in list3:
    print(items ,lollypops)                                                                                

    #change list into dictionary

    dict1 = dict(list3)
    print(type(dict1))