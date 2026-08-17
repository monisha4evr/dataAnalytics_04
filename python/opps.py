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

# Encapsulation
#-------------------
# Access Specifier
# 1. Public - Anyone can Access
# 2. Protected - class and inherited class
# 3. Private - within the same class

# How to denote
# protected variable : _ 
# private variable : __ 
        # 1. getter/Setter (get/set)
        # 2. Name Mangling (_classname__privateVariableName)

class UserProfile:
    def __init__(self,uname,mbl,pwd):
        self.uname=uname
        self._mbl=mbl
        self.__pwd=pwd

    def get_password(self):
        print("Password is:",self.__pwd)
    
    def set_password(self,newpwd):
        self.__pwd=newpwd

up=UserProfile("Kavi",'9809878909','kavi123')
print(up.uname)
print(up._mbl)
print(up._UserProfile__pwd) # Name Mangling
up.get_password()
up.set_password("123Kavi")
up.get_password()
# print(up.__pwd) # It will Throw AttributeError

#Inheritance
# 1. Single inheritance
# 2. Multiple Inheritance
# 3. multilevel Inheritance 
# 4. Hierarchical Inheritance

# 1. Single inheritance
# Base/Parent/Super class
# Derived/child Class

# one base Class -> one Derived Class

class Parent:
    def parent_display(self):
        print("I am from Parent Class")

# p=Parent()
# p.parent_display()

class Child(Parent):
    def child_display(self):
        print("I am Child")

c=Child()
c.child_display()
c.parent_display()

# 2. Multiple Inheritance
# -> Multiple Parent => Single Child

class Father:
    def display(self):
        print("Father")

class Mother:
    def m_display(self):
        print("Mother")

class Child(Father,Mother):
    def c_display(self):
        print("Child")

c=Child()
c.c_display()
c.display()
c.m_display()

# 4. Hierarchical Inheritance
# -> Single Parent => Multiple Child

class Animal:
    def make_sound(self):
        print("Animals Makes Sounds")

class Dog(Animal):
    def bark(self):
        print("Dog says boww boww")

d=Dog()
d.make_sound()
d.bark()

class Cat(Animal):
    def meow(self):
        print("cat says Meoeeeew")

c= Cat()
c.make_sound()
c.meow()

# 3. multilevel Inheritance
# -> chain -> grandparent=> parent=>child=>grandchild

class Grandparent:
    def display(self):
        print("Gparent")

class Parent(Grandparent):
    def p_parent(self):
        print("parent")

class Child(Parent):
    def c_parent(self):
        print("child")

class GrandChild(Child):
    def gc_parent(self):
        print("Grand Child")

c = GrandChild()
c.display()
c.p_parent()
c.c_parent()
c.gc_parent()

# Polymorphism
# 1. Overlaoding Same
# 2. overriding

# 1. Overlaoding Same
# ------------------------
class Calculation:
    def add(self,a,b,c=0,d=None,*e):
        print(a,b,c,d,e)

c= Calculation()
c.add(5,10)
c.add(1,2,3)
c.add(1,2,3,4)
c.add(1,2,3,4,5,6,7,8)

# 2. overriding (runtime  Polymorphism)
class Animal:
    def make_sound(self):
        print("Animals Makes Sounds")

class Cat(Animal):
    def make_sound(self):
        print("cat says Meoeeeew")

c= Cat()
c.make_sound()

# 2. Abstraction - hiding unnecessary information - show important 
# normal method and Abstract method 

# Decorator : Extend the Functionality without modifying the Original method

from abc import ABC,abstractmethod

class Vehicle(ABC):
     @abstractmethod
     def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def display(self):
        print(f"Brand Name: {self.brand} \nColor:{self.color}")

    def start_engine(self):
        print("Engine Started..................") 

c=Car("BMW","Red")
c.display()
c.start_engine()


class Parent:
    def __init__(self):
        print("Parent")

class Father(Parent):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(Parent):
    def __init__(self):
        super().__init__()
        print("mother")

class Child(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Child")

c=Child()
# Method Resolution Order (MRO)
print(Child.__mro__)

#Super Class

class Parent:
    def display(self):
        print("Parent")

class Child (Parent):
    def display(self):
        super().display()
        print("Child")

c= Child()
c.display()