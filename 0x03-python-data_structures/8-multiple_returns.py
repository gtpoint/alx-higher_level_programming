#!/usr/bin/python3
#8-multiple_returns.py


def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character."""

    if sentence == "":
       return (0, None)

    else:
       return (len(sentence), sentence[0])
