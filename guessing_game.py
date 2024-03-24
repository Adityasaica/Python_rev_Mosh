target=9
i1=1
while i1<=3:
    g=int(input("Guess:"))
    if g==target:
        print("found successful")
        break
    i1+=1
else:
    print("Sorry not found")
#we can any of the code snippet
#
# if i1==4:
#     print("Sorry not found!")