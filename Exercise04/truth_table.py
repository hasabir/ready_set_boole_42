from truths import Truths

OPERATORS = {
    "&": lambda x, y: x & y,
    "|": lambda x, y: x | y,
    "ˆ": lambda x, y: x ^ y,
    ">": lambda x, y: x > y,
    "=": lambda x, y: x == y,
    "!": lambda x: not x, 
}



def print_truth_table(formula: str):
    try:
        stack = []
        # for i in formula:
        #     if i.isdigit():
        #         stack.append(bool(int(i)))
        #     else:
        #         stock1 = stack.pop()
        #         if i == "!":
        #             stack.append(OPERATORS[i](stock1))
        #         else:
        #             stock2 = stack.pop()
        #             stack.append(OPERATORS[i](stock1, stock2))
        # if len(stack) != 1:
        #     raise ValueError("Invalid formula")
        return stack
    except Exception as e:
        raise e




def main():
    try:
        formula = input("Enter a formula: ")
        for i in formula:
            # print(f"i = {i} and lower i = {i.lower() == }")
            if i not in "01&!|^>=":
                if not i.isalpha():
                    raise SyntaxError("Syntax error")
                elif i.lower() == i:
                    raise SyntaxError("Syntax error")
        print(sum(i.isalpha() for i in formula))
        
        # print(Truths(['a', 'b', 'c'], ['(a and b)']))
    except Exception as e:
        print(f"Error: {e}")
    
    
    
if __name__ == "__main__":
    main()