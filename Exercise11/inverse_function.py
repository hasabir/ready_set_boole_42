from numpy import uint16, float64


def reverse_map(n: float64) -> tuple[uint16, uint16]:
    return uint16(n // 65536), uint16(n % 65536)


def main():
    try:
        # num = input("Enter number to reverse map :")
        
        x, y = reverse_map(float64(input("num = ")))
        
        print(f"x: {int(x)}, y: {int(y)}")
    except Exception as e: 
        print(f"An error occurred: {e}")
        


if __name__ == "__main__":
    main()

