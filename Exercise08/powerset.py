from numpy import uint32

def powerset(set: list[uint32]) -> list[list[uint32]]:
    try:
        result = [[]]

        for element in set:
            new_subset = []
            for curr in result:
                subset = curr + [element]
                new_subset.append(subset)
            result += new_subset

        return result
    except Exception as e:
        raise e


def main():
    try:
        set = input("Enter a set of elements (comma-separated): ")
        if len(set) != 0:
            set = set.split(',')
        result = powerset([uint32(x) for x in set])
        print("Powerset:", result)
  
    except Exception as e:
        print("An error occurred:", e)



if __name__ == "__main__":
    main()