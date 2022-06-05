#!/usr/bin/python3
def element_at(my_list, idx):
    for x in my_list:
        if idx == my_list.index(x):
            return(x)
        elif idx > len(my_list):0
            return None
        elif idx < 0:
            return None
