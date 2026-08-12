a=[91,2,13,4,55,6,7]
print(a[0])
print()
for i in a:
    print(i)

a=["Ben","kavi","hari","dhruv","Laya"]
b=["Trichy","Erode","Chennai","Madurai"]
c=["DA","AI/Ml","Java","Python"]

print(list(zip(a,b,c)))

for i in zip(a,b,c):
    print(i)

for i in range(1,6):
    print(i)

for i in enumerate(range(1,6)):
    print(i)

for i,v in enumerate(range(1,6)):
    print(i,v)

for i in range(1,6):
    if i%2==0:
        print("Even")
    else:
        print(i)

#ternary
for i in range(1,6):
    print("Even" if i%2==0 else i)

print(list(range(1,11)))
print(tuple(range(1,11)))

for i in range(1,11):
    print(i*2)

# list Comprehension
print([i*2 for i in range(1,11) if i%2==0])
print({i*2 for i in range(1,11)})