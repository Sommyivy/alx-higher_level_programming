#!/usr/bin/python3
import sys
my_list = sys.argv
print("{}: Argument".format(len(my_list)-1))
for item in my_list:
    indx = my_list.index(item)
    if indx != 0:
        print("{}: {}".format(indx, item))
                        
