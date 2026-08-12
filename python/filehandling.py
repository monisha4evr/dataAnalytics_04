# File handling 
mode: 
# w -> Write
# a -> Append 
# r -> Read 


file=open("ben.txt",'w')
file.write("Python Learning is Interesting....")
file.close()

file=open("ben.txt",'a')
file.write("\nSkillfort")
file.close()



# read:
# 1. read() -> REad All 
# 2. readline() -> Read first Line only
# 3. readlines() -> Read Everything and make them list
file=open("ben.txt",'r')
print(file.read())
file.close()

file=open("ben.txt",'r')
print(file.readline())
file.close()

file=open("ben.txt",'r')
print(file.readlines())
file.close()

with open("kavinya.txt",'w') as file:
    file.write("Happy Learning")

with open("kavinya.txt",'r') as file:
    print(file.read())