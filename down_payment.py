price=int(input("Enter the Price of the Houde? "))
good_credit=int(input("Enter wether he had a good credit?(0/1) "))

if good_credit==1:
    down_payment=int(price*0.1)
else:
    down_payment=int(price*0.2)
print(f"The DownPayment for the house is ${down_payment} as you having a good credit score is {good_credit}")