OPERATORS = {
    "&": lambda x, y: x & y,
    "|": lambda x, y: x | y,
    "^": lambda x, y: x ^ y,
    ">": lambda x, y: x > y,
    "=": lambda x, y: x == y,
    "!": lambda x: not x, 
}



def eval_formula(formula: str)-> bool:
    try:
        stack = []
        for i in formula:
            if i.isdigit():
                stack.append(bool(int(i)))
            else:
                stock1 = stack.pop()
                if i == "!":
                    stack.append(OPERATORS[i](stock1))
                else:
                    stock2 = stack.pop()
                    stack.append(OPERATORS[i](stock1, stock2))
        if len(stack) != 1:
            raise ValueError("Invalid formula")
        return stack.pop()
    except Exception as e:
        raise e
    


def main():
    try:
        formula = input("Enter a boolean formula: ")
        if any(i not in "01&!|^>=" for i in formula):
            raise SyntaxError("Syntax error")
        print(f"Result: {eval_formula(formula)}")
    except Exception as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    main()