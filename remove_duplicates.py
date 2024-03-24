l=[1,1,2,3,4,4,5,6,7,8,8,9,9,9,10,11,11,11,12,13,14,14,15]
l_final=[]
for i in l:
    if not  i in l_final:
        l_final.append(i)
print(l_final)
