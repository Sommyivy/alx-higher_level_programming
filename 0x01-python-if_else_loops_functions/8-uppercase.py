#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        low = ord(alphabet)
        jb = chr(ord(alphabet) - 32)
        if low >= 97 and low <= 123:
            print("{}".format(jb), end="")
        else:
            print("{}".format(alphabet), end="")
     display("\n")                                                                     
