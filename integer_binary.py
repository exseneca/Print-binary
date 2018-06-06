"""integer to binary prints out the integer in binary"""
from sys import argv

def integer_to_binary(n):
    lst = []
    remainder = divide_remainder(n, lst)
    remainder.reverse()
    return ''.join(map(str ,remainder))


def divide_remainder(n, lst):
    """recursive function which return a list of remainders of 2""" 
    floor = n // 2
    remainder = n % 2
    if floor == 0:
        lst.append(remainder)
        return  lst
    else:
        lst.append(remainder)
        return divide_remainder(floor, lst)

def main():
    try:
        n = int(argv[1])
    except ValueError:
        print("Please only type a number")
        return 1

    print(integer_to_binary(n))

if __name__ == "__main__":
    main()