num=int(input("Phone:"))

words={

    '1':"one",
    '2':"two",
    '3':"three",
    '4':"four",
    '5':"five",
    '6':"six",
    '7':"seven",
    '8':"eight",
    '9':"Nine",
    '0':"zero"

}
num=str(num)
for i in num:
    print(words[i],end=" ")



