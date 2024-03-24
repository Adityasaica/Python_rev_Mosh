#car game
is_started=False
is_stop=True

while True:
    choice=input("Enter your option:")
    if choice=='start':
        if is_started:
            print("car is in start mode ready to go")
        else:
            print("Car started..ready")
            is_started=True
            is_stop=False
    elif choice=='stop':
        if is_stop:
            print("Already in Stop mode!")
        else:
            print("Car is now Stopped.")
            is_stop=True
            is_start=False
    elif choice=='quit':
        print("Exit")
        break
    else:
        print("I Could not understand")
