word=input("Enter the String:")
l=len(word)

if l<3:
    print("Length of the word must be at least 3")
elif l>50:
    print("Reduce the size as the length of the stiring max of 50")
else:
    print("Its a perfect Size")