from numpy import uint32


def adder(a: uint32, b: uint32) -> uint32:
    try:
        carry = (a & b) << 1
        result = a ^ b

        while carry:
            result, carry = result ^ carry, (result & carry) << 1
            
        return result
    except Exception as e:
        print(f"Error: {e}")




def main():
    try:
        a = uint32(input("Enter a number: "))
        b = uint32(input("Enter another number: "))
        print(f"Result: {adder(a, b)}")
    except Exception as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    main()