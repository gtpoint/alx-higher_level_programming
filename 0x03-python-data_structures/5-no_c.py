#!/usr/bin/python3
#5-no_c.py


def no_c(my_string):
   """removes all characters c and C from a string."""

   _list = [letter for letter in my_string if letter != 'c' and letter != 'C']

   print("".join(_list))
