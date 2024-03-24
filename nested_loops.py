for i in range(4):
    for j in range(4):
        print(f"({i}, {j})")
#fraw F shape in python

for i in range(6):
    if(i==0 or i==2):
        for j in range(6):
            print("x",end="")
        print()
    else:
        for k in range(3):
            print("x",end="")
        print()
print()
print()
#alternate method
l=[5,2,5,2,2]
for i in l:
    for j in range(i+1):
        print("x",end="")
    print()

names=['john','mob','mosh',"sara",'mary']
print(names)
print(len(names))
#indexing of the list
print(names[1])
print(names[0])
print(names[-1])
print(names[-2])
print(names[2:])

print(names[:])
#above will not modify the original contents
names[0]="Johns"
print(names)
#to find the largest number in a list
li=[1,3,7,9,44,5,6,34,67]
max=li[0]
for j in li:
    if j>max:
        max=j
print(f"the maximum of the list is {max}")

