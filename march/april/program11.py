#write a programe to check a name in the list
list = ["shivam","ansh","satyam","harsh","nikunj"]
for i in range(len(list)):
    print(list[i])
    if list[i] == 'harsh':
        print("found the name")
        break
    else:
        continue
