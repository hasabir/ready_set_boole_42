
class Truth_table:
    def __init__(self, formula: str):
        self.formula = formula
        self.truth_table = {}
        self.operators = {
            "&": lambda x, y: x & y,
            "|": lambda x, y: x | y,
            "^": lambda x, y: x ^ y,
            ">": lambda x, y: not x or y,
            "=": lambda x, y: x == y,
            "!": lambda x: not x, 
        }
        self.num_of_rows = 0
    
    def _get_table(self):
        try:
            self.truth_table = {i: [] for i in self.formula if i.isalpha()}
            step_size = 1
            self.num_of_rows = 2 ** len(self.truth_table)
            
            for column in reversed(self.truth_table):
                prev = 1
                i = 0
                while i < self.num_of_rows:
                    prev ^= 1
                    for _ in range(step_size):
                        self.truth_table[column].append(prev)
                    i += step_size
                step_size *= 2
            return self.truth_table
        except Exception as e:
            raise e

    def check_formula(self):
        try:
            for i in self.formula:
                if i not in "&!|^>=" and (not i.isalpha() or i.lower() == i):
                    raise SyntaxError(f"Syntax error")
        except Exception as e:
            raise e

    def evaluate_formula(self, formula: str)-> bool:
        try:
            stack = []
            for i in formula:
                if i.isdigit():
                    stack.append(bool(int(i)))
                else:
                    if i == "!":
                        stack.append(self.operators[i](stack.pop()))
                    else:
                        stack.append(self.operators[i](stack.pop(), stack.pop()))
            if len(stack) != 1:
                raise ValueError("Invalid formula")
            return stack.pop()
        except Exception as e:
            raise e

    def get_result(self):
        try:
            self.check_formula()
            self._get_table()
            
            self.truth_table['='] = []
            for i in range(self.num_of_rows):
                boolean_formula = ""
                for j in self.formula:
                    if j.isalpha():
                        boolean_formula += str(self.truth_table[j][i])
                    else:
                        boolean_formula += j
                result = int(self.evaluate_formula(boolean_formula))
                self.truth_table['='].append(result)
            return self.truth_table
        except Exception as e:
            raise e


def print_truth_table(formula: str):
        try:
            truth = Truth_table(formula)
            truth.get_result()
            for i in truth.truth_table:
                print(f"| {i} ", end="")
            print("|")
            for i in truth.truth_table:
                print("|---", end="")
            print("|")
            num_of_rows = 2 ** (len(truth.truth_table) - 1)
            for i in range(num_of_rows):
                for j in truth.truth_table:
                    print(f"| {int(truth.truth_table[j][i])} ", end="")
                print("|")
        except Exception as e:
            raise e



def main():
    try:
        formula = input("Enter a formula: ")
        print_truth_table(formula)
    except Exception as e:
        print(f"Error: {e}")
    
    
if __name__ == "__main__":
    main()