#!/usr/bin/python3
#3-print_reversed_list_integer.py

def new_in_list(my_list, idx, element):
    """
        replaces an element in a list at a specific
        position without modifying the original list (like in C).
    """

    copy_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
       return (copy_list)

    copy_list[idx] = element

    return (copy_list)
