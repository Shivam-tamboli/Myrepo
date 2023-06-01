#How to make enumerate function
l1 = ["bhindi", "chopstick", "aloo", "chowmien"]
for index, item in enumerate(l1):
    if index%2==0:
        #now we will use id f strings
        print(f"jarvis please buy {item}")
