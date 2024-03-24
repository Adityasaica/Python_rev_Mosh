has_high_income=True
has_good_credit=False
if has_high_income and has_good_credit:
    print("Eleigible for loan")
else:
    print("sorry!!")

if has_high_income or has_good_credit:
    print("Eleigible for loan")
else:
    print("sorry")

#logical and operator both must be true
#or operator any one must be true
#not operator wil reverse the expression that we give

has_criminal_record=False

if has_high_income and not(has_criminal_record):
    print("Approved!")