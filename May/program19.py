# Inheritance
# class base:
# 	// Members and Functions
# 	Pass
# class derived1(base):
# 	// Members and functions of both base and derived1 classes
# 	pass
# class derived2(derived1):
# 	// Members and functions of base class, derived1 class, and derived2 class.
# 	Pass

class Animal:
    def speak(self):
        print("Animal speaking")
#dog class can use the functions of the animal class
class Dog (Animal):
    def bark(self):
        print("Dog barking")
    
d = Dog()
d.bark()
d.speak()



