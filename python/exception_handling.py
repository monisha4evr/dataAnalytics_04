# Exception Handling

# - Error Handling

# try - block which we expect Error
# except - catch the error
# else - Execute when no error
# finally - execute everytime
# raise - custom Error


# Exception type:
# 1. generic
# 2. Specific


# 1. TypeError - int+str
# 2. ZeroDivisionError - divide by zero
# 3. ValueError - invalid type conversion


try:
    print(int("abc"))
    print("welcome")
except ValueError:
    print("Cant convert string to int")
else:
    print("No Error")
finally:
    print("Skillfort")

try:
    a=10
    if a>0:
        print(a+"aaa")
    else:
        print(10/a)
except ValueError,TypeError:
    print("Error occured")
except ZeroDivisionError:
    print("Zero division")
except Exception as e:
    print(e)

try:
     print(10+"apple")
    # print(10/0)
except Exception as e:
    print(e)


class BenRock(Exception):
    pass


def checkage(age):
    if age<18:
        raise BenRock("ERRRORRRRRRRRRRRRR")
    else:
        print("you are Eligible")

try:
    checkage(15)
except Exception as e:
    print(e)


def checkage(age):
    if age<18:
        raise ValueError("Grow up Kid")
    else:
        print("you are Eligible")

try:
    checkage(15)
except Exception as e:
    print(e)