import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from Exercise04.truth_table import Truth_table


def sat(formula: str) -> str:
    table = Truth_table(formula)
    table.check_formula()
    table_result = table.get_result()
    if any(table_result['=']) == True:
        return True
    return False

def main():
    try:
        formula = input("Enter a formula: ")
        print(sat(formula))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
