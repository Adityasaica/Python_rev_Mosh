matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
#indexing the

print(matrix[0][1])
#by mxn formular matrix[m][n]
matrix[0][1]=20
print(matrix)


for row in matrix:
    #print all rows
    print(row)
#list methods

numbers=[1,2,3,4,5]
numbers.append(6)
#used to add new number at the end

print(numbers)
numbers.insert(0,4)
#used to insert a number/element at the desired index
print(numbers)

#to remive an element
numbers.remove(4)
print(numbers)
#removes a particular number at its first instance
numbers.pop()
print(numbers)
print(numbers.index(4))
print(50 in numbers)
print(2 in numbers)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
num=numbers.copy()
#if you dont use the copy method any change in original list could cause the same

print(num)
print(numbers.count(3))
