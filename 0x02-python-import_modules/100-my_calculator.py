#!/usr/bin/python3

if __name__ == "__main__":
    
    """
       imports all functions from the file 
       calculator_1.py and handles basic operations.

    """
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
       print("Usage: ./100-my_calculator.py <a> <operator> <b>")
       sys.exit(1)

    _list = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in list(_list.keys()):
       print("Unknown operator. Available operators: +, -, * and /")
       sys.exit(1)

    else:
       a = int(sys.argv[1])
       b = int(sys.argv[3])
       for ope in list(_list.keys()):
           if ope == sys.argv[2]:
              print("{} {} {} = {}".format(a, sys.argv[2], b, _list[ope](a, b)))
