from numpy import uint32


def gray_code(n: uint32) -> uint32:
    try:
        return uint32(n ^ (n >> 1))
    except Exception as e:
        print(f"Error: {e}")


def main():
    try:
        n = uint32(input("Enter a number: "))
        print(f"Result: {gray_code(n)}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()