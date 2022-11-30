#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        low = ord(alphabet)
        if low >= 97 and low <= 123:
            num = 32
        else:
            num = 0
            print(chr("{}".format(low - 32), end="")
    print("")
