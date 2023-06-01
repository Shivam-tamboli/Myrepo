def funargs(**kwargs):
    print("now i would like to introduce:")
    for i in kwargs.items():
     print(i)

     kw = {"rohan":"monitor","shivam":"coordinator","ansh":"instructor"}
     print(**kw)