from numpy import uint32

def powerset(set: list[uint32]) -> list[list[uint32]]:
    try:
        result = [[]]
        
        for element in set:
            result += [curr + [element] for curr in result]
        return result
    except Exception as e:
        raise e


def main():
    try:
        set = input("Enter a set of elements (comma-separated): ")
        set = set.split(',')
        result = powerset(uint32(x) for x in set)
        print("Powerset:", result)
  
    except Exception as e:
        print("An error occurred:", e)



if __name__ == "__main__":
    main()