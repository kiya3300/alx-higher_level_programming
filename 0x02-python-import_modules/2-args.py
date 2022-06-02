#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))

    for i in range(1, num):
=======
import sys
if __name__ == "__main__":
    size = len(sys.argv)
    if (size == 1):
        print("{} arguments.".format(size - 1))
    elif (size == 2):
        print("{} argument:".format(size - 1))
    else:
        print("{} arguments:".format(size - 1))

    for i in range(1, size):
>>>>>>> e333a4d9f1cfa1480ef94cd98aad676403174350
        print("{}: {}".format(i, sys.argv[i]))
