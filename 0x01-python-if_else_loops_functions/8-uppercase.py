#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        low = ord(alphabet)
        if low >= 97 and low <= 123:
            print(chr(ord(alphabet) - 32), end="")
        else:
            print(alphabet, end="")
    print("")
                                                                          
