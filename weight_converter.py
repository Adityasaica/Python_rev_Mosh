w=int(input("Weight:"))
option=input("(l)bs or (k)gs? ")
option=option.upper()
if option=='L':
    final=w/2.2
    print(f"the weight in Kgs is {final}")
elif option=='K':
    final=w*2.2
    print(f"the weight in ponds is {final}")

