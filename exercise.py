class Person:

    def __init__(self,n,istalk):
        self.name=n
        self.talketive=istalk

    def print_name(self):
        print(f"your name is {self.name}")

    def is_talketive(self):
        print(f"{self.name} is talketive was {self.talketive}")


obj1=Person("Adithya",True)
print(obj1.name)
print(obj1.talketive)
