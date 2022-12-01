#!/usr/bin/python3
import sys
my_list = sys.argv
jb = len(my_list)-1
if jb == 1:
    print("{}: argument".format(len(my_list)-1))
else:
    print("{}: arguments".format(len(my_list)-1))
for item in my_list:
    indx = my_list.index(item)
    if indx != 0:
        print("{}: {}".format(indx, item))
                        
