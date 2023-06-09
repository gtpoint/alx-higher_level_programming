#!/usr/bin/python3


if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0

    if len(sys.argv) - 1 == 0:
       print("0")

    else:
        for i in range(len(sys.argv) - 1):
            total += int(sys.argv[i + 1])
        print("{}".format(total))
