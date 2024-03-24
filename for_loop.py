name='python'
for letter in name:
    print(letter)
for item in 'list of items':
    print(item)
#iteration through the lists

l=['srinivasarao','rajyalakshmi','adithya','amrutha']
for i in l:
    print(i)

#printing 10 numbers

for i in range(10):
    print(i**2)
for i in range(1,10,2):
    print(i**2)
#total in a list
l=[10,20,30,40]
total=0

for items in l:
    total+=items
print(f"the sum of the list items is {total}")