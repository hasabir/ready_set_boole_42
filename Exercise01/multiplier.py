from numpy import uint32
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))

from Exercise00.adder import adder


def multiplier(a: uint32, b: uint32) -> uint32:
    try:
        result = 0
        while b:
            if b & 1:
                result = adder(result, a)
            a <<= 1
            b >>= 1
        return result
    except Exception as e:
        print(f"Error: {e}")



def main():
    try:
        a = uint32(input("Enter a number: "))
        b = uint32(input("Enter another number: "))
        print(f"Result: {multiplier(a, b)}")
    except Exception as e:
        print(f"Error: {e}")



if __name__  == "__main__":
    main()