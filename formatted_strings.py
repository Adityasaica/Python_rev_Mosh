first='john'
last='smith'
message =f"{first} [{last}] is a coder"
#above is an illustrations for the formatted strings
print(message)
course='python for begginers'
#below used to find the length of the string list etc it is a general purpose strings

print(len(course))
print(course.upper())
print(course.capitalize())
print(course)
print(course.lower())
print(course.islower())
#below used to find the index of the charecter
print(course.find('p'))
print(course.find('o'))
#replace

print(course.replace('begginers','Absolute Beginners'))
print('python' in course)
#tha above code gives the true or false
if('python' in course):
    print("python was present in the string")
print(course.title())
