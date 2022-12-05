#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new =[]
    a = True
    b = False
    for i in my_list:
        if i % 2 == 0:
            new.append(a)
        else:
            new.append(b)
    return(new)
