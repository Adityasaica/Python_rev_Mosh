def greet_user(n="default",last_name="default"):
    print("Hi there")
    print(f"Welcome Onboard! {n} {last_name}")


greet_user()

#when even we use a function we must give two line gaps


#use of the parameters
name=input("Enter the name:")
ln=input("Enter the last name:")
greet_user(name,ln)

#parameters were at the defnitions
#arguments were te values we give


#use of the return value

def square(n):
    return n**2

print(square(5))
print(square(5.12))

result=square(6)
print(result)

#if there is no return statement and yet tried to print value gives None
