#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
    print("{}".format(result))
=======
import sys
if __name__ == "__main__":
    size = len(sys.argv)
    sum = 0
    if size > 1:
        for i in range(1, size):
            sum += int(sys.argv[i])
    print("{}".format(sum))
>>>>>>> e333a4d9f1cfa1480ef94cd98aad676403174350
