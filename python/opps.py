# oops=> Object Oriented Programming 

#     - Structured and real world entity

# class => Blueprint 
# object => instance of Class 
# method => function inside class 
# variable/attribute


# Syntax:
class Classname:
    pass
    # variable
    #def functionname():


class Sample:
    name="kavi"
    address="chennai"

print(Sample.name)
print(Sample.address)
Sample.name="Ben"
print(Sample.name)
Sample.city="Navallur"
print(Sample.city)

print(f" Name: {Sample.name} Address : {Sample.address}")
setattr(Sample,"pincode",684933)
print(Sample.pincode)
delattr(Sample,"pincode")
print(getattr(Sample,"city"))
print(Sample.pincode)  # AttributeError: type object 'Sample' has no attribute 'pincode'


class Test:
    def display():
        print("Welcome")

Test.display()




# method types:
# 1. instance  - self
# 2. classmethod - cls
# 3. staticmethod

class Test:
    def display(self):
        print("Welcome")

t=Test()
t.display()
t1=Test()
t1.display()
t2=Test()
t2.display()
t3=Test()
t3.display()

class StudentDetails:
    def display(self,name,address):
        print(name)
        print(address)


sd=StudentDetails()
sd.display("Ben","Trichy")
sd1=StudentDetails()
sd1.display("Kavi","Erode")

class Userprofile:
    def __init__(self,uname,mbl,addrs):
        self.name=uname
        self.mbl=mbl
        self.addrs=addrs

    def display(self,pincode):
        print(f" Name: {self.name} \n Mobile: {self.mbl} \n Address: {self.addrs} \n Pincode: {pincode}")

up=Userprofile('Abhi',8909878987,"Chennai")
up.display(654654)


# Class Method
class Vegetable:
    veg1="Potato"
    veg2="Tomato"
    veg3="Carrot"

    @classmethod
    def display(cls):
        print(cls.veg1,cls.veg2,cls.veg3)

v=Vegetable()
v.display()


# Static Method

class Calculation:
    @staticmethod
    def add(a,b):
        print("Addition: ", a+b)

c=Calculation()
c.add(5,10)

# pillars of Oops concept
# 1. Encapsulation - Bind data Together
# 2. Abstraction - hiding unnecessary information - show important 
# 3. Polymorphism - many form 
# 4. Inheritance - single,multiple, multi-level,hierarchial