# we cannot use the input because it can come in different forms
#making the emoji program into reusble function

def emoji_converter(message):
    dict={
        ':)':"😀",
        ':(':"☹️",
        ';)':"😎"
    }
    message_converted=message.split(" ")
    ans=dict.get(message_converted[-1])
    if ans==None:
        print("not Found")
    else:
        print(ans)


while(True):
    mess=input("Enter the text:")
    if mess=='stop':
        break
    else:
        emoji_converter(mess)

