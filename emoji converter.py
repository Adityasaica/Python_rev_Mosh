inp=input(">")

inp=inp.split(" ")
req_emoji=inp[-1]
emoji_d={

    ':)':"😃",
    ':(':"☹️",
    ';)':"😉"

}
print(emoji_d[req_emoji])
