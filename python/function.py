# Function:

# reusable block of code: to perform some Specific Task

# function:
# 1. built-in 
# 2. user defined function 
# 3. lambda function 
# 4. recursion

# 1.built-in function:
# -----------------

print()
input()


# 2.userdefined function

# 1. function Declaration/definition
# 2. function calling

# Syntax:
# 1. function Declaration/definition
def functionname():
    pass

# 2. function calling
functionname()

def display():
    print("I am insdide the Function")
display()

def greet():
    print("Welcome")

greet()
greet()
greet()
greet()


def employee(name,salary,inc_amt):  # parameter
    print(f"Name: {name} ->  Total Salary: {salary}  {inc_amt}")


employee("Ben",50000,20000) # arguments-> actual value

a="Sneha"
b=70000
c=5000
employee(a,b,c)


# arguments Type
# 1. positional argument 
# 2. keyword argument
# 3. default argument 
# 4. arbitary argument

def display(a,b,c):
    print(a,b,c)
display(10,20,30)
display(b=10,c=20,a=30)


def userprofile(name,username="user"):
    print(name,username)

#userprofile("Karthika")
userprofile("Bhuvana","bhuvi")

#arbitary Argument
def add(*a):
    print(a)
add(2,4,6,8,1,3)


def display(**q):
    print(q) 

display(a=5,b=10,c=15)

# Position only
def add(a,b,c):
    print(a,b,c)
add(2,4,c=6)

# keyword only
def display(*,m,n,o):
    print(m,n,o) 

display(m=5,n=10,o=15)




# function Types:
# 1. without argument without return
# 2. with argument without return
# 3. without argument with return
# 4. with argument with return


# keyword: return

def greet():
    print("Hi Function!")
greet()

# with argument without return
def greet(name):
    print("Hi ",name)
greet("Bhuvana")


def add(a,b):
    print(a+b)

add(45,500)
add(50,50)
add(150,250)

#3. without argument with return

def multiplication():
    a=10
    b=20
    return(a*b)

print(multiplication())
a=multiplication()
print(a)

# 4. with argument with return
def multiplication(a,b):
    return(a*b)

print(multiplication(10,20))
print(type(multiplication))
a=multiplication(10,40)
print(a)


#  3. lambda function
    # - Anonymous Funciton 
    # - singleline Expression

    # syntax: lambda argument:Expression

a=5
print(type(a))

a=lambda x:x*2
print(type(a))
print(a(5))

#4.recursion
# function call itself
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)


# 5*4*fact(3)
print(fact(5))




def test():
    print(10)
    return
    print(20)
    print(30)

test()

def calculation(a,b,operator):
    if operator == "add":
        print("Addition: ",a+b) 
    elif operator == "sub":
        print("Subtraction: ",a-b)
    elif operator == "mul":
        print("Multiplication: ",a*b)

    elif operator == "div":
        print("division: ",a/b)

    elif operator == "fdiv":
        print("floor Division: ",a//b)
    else :
        print("Modulus: ",a%b)
    

calculation(10,20,"add")
calculation(50,20,"sub")
calculation(50,20,"div")
calculation(51,20,"fdiv")
calculation(51,20,"mod")