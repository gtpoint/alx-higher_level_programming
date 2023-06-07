#!/usr/bin/python3  

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) == 'e' or chr(letter) == 'q':
       continue
    print("{}".format(chr(letter)), end="")
