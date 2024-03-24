#defining a new type
#self is the reference to the current object

#for naming a class we need to capitalize the first letter of the word
#called as the pascal naming convention
class Point:
    def __intit__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


# obj1=Point(10,20)
# obj1.move()
# obj1.draw()
# obj1.x=10
# obj1.y=20
#
# point2=Point(10,20)
# point2.x=1
# print(point2.x)

#constructors

# point=Point()
# print(point.x)
#with above we get a attribute error

#we use constructor to solve this

point=Point(10,20)
print(point.x)