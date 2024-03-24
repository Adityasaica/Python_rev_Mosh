class Point:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def move(self):
        print("Move")
    def draw(self):
        print("draw")


point1=Point(10,20)
print(point1.a)