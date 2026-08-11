a=10
b=20
print(a,b)
a,b=b,a
print(a,b)


# list
# - denoted by []
# - Mutable (Changable)
# - allow Duplicate 
# - Hetrogeneous



# to add value in List 
# 1. append
# 2. insert 
# 3. extend

a=[1,2,3,2,3,1]
print(a[2])
print(type(a))
print(a)
a.append(5)
print(a)
a.append([5,6])
print(a)
a.extend([9,8])
print(a)
a.insert(0,[9,9])
print(a)


Mutable data types:
List,
tuple,
Dict

immutable Data types:
int,str,bool,float

a=10
b=10 
print(id(a))
print(id(b))

a=20
print(id(a))
print(id(b))

a=[1,2,3]
b=[1,2,3]
a.append(7)
print(id(a))
print(id(b))

a=[1,2,3,4]
b=a.copy()
b.append(7)
print(a,b)

c=a
c.append(10)
print(a,c)

a=[2,4,6,8,10]
print(a)
a.pop(0)
print(a)
a.remove(10)
print(a)

a=[1,2,2,2,2,2,2,3,4]
print(a.count(2))

a.clear()
print(a)

a=[10,20,30,40,50]
a.reverse()
print(a)

a=[90,10,80,20,60,30,70,40,50]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a=(10,20,30,40,50)
b=a.count(30)
print(b)
print(a.count(20))
print(a.index(50))
print(a[4])
a.index(0)

a={1,2,3,4}
b={1,2,3,7,9}
print("Union :",a.union(b),a|b)
print("Intersection: ",a.intersection(b))
print("Difference: ",a.difference(b))
print("Symetric Difference: ",a.symmetric_difference(b)) 

a={"apple":"red","carrot":"orange","beetroot":"Pink"}
print(a)
print(type(a))
a['beetroot']="Vine"
print(a)
a['brinjal']="purple"
print(a)

for i in a.values():
    print(i)

for i in a.keys():
    print(i)

for k,v in a.items():
    print(k,v)