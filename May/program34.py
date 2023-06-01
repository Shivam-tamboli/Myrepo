#How to pickle a object
import pickle

cars = ["Audi","BMW","Maruti","Ninja"]
file = "mycar.pkl"
fileobj = open(file, 'wb')  #It will be in a binary form
pickle.dump(cars,fileobj)  #dump funcation takes two arrgument .first the pack object .the file object
fileobj.close()


file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)