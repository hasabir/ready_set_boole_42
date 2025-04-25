
from numpy import uint16, float64


def map(x: uint16, y: uint16) -> float64:
    return float64(int(x) * 65536 + int(y))


def main():
    try:
        print("Enter number in interval [0; 2^16] ")
        x = uint16(int(input("x = ")))
        y = uint16(int(input("y = ")))
        num = map(x, y)
        
        print(f"num = {num}")
        num = num / 4294901760 # Normalization to be ⊂ [0; 1]
        print(f"num after normalization = {num}")
    except Exception as e: 
        print(f"An error occurred: {e}")
        


if __name__ == "__main__":
    main()

