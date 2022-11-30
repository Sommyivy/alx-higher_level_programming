#!/usr/bin/python3
def  fizzbuzz():
    for i in range (1,102):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz",end=" ")
        elif  i % 3 != 0 and i % 5 != 0:
            print(i, end=" ")
        elif i % 3 == 0:
            print("fizz", end=" ")
        elif i % 5 == 0:
            print("buzz", end=" ")
        else:
            print("\n")
