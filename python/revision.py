# try 
# except 
# finally 
# else
# raise  


types of Exception:

1. Generic 
2. Specific 



try:
    print(123+"456")
except ValueError:
    print("Cant do this Operation")
except TypeError:
    print("TypeError")


try:
    print(123+"456")
except ValueError,TypeError:
    print("Cant do this Operation")

try:
    print(123+"456")
except Exception as e:
    print("Error Message:",e)
else:
    print("No Error Found")
finally:
    print("I run Always")


class AgeLimit(Exception):
    pass 

def checkage(age):
    if age<=18:
        raise AgeLimit("Must Above 18")
    else:
        print("You are eligible")
try:
    checkage(21)
except Exception as e:
    print(e)

     