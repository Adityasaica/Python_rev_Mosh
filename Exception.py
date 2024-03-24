


#if exit code 0 means no errors
#if exit code 1 means it ran into errors


#to handle errors we use:
#if there is a error i try block except block will be invoked


try:
    age = int(input("Age:"))
    income=20000
    risk=income/age
    print(age)
except ValueError:
    print("You entered a String")

except ZeroDivisionError:
    print("Age cannot be Zero")


#we should know or guess the capable errors and eliminate them as soon as possible


#comments
print("Sky is Blue")
