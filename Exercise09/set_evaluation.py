OPERATORS = {
    "!": lambda universe, x: [item for item in universe if item not in x],
    "&": lambda x, y: [element for element in x if element in y],
    "|": lambda x, y: x + [element for element in y if element not in x],
    "^": lambda x, y: [element for element in OPERATORS["|"](x, y) if element not in OPERATORS["&"](x, y)],
    ">": lambda x, y, universe: OPERATORS["|"](OPERATORS["!"](universe, x), y),
    "=": lambda x, y, universe: OPERATORS["&"](OPERATORS[">"](x, y, universe), OPERATORS[">"](y, x, universe))
}


def eval_set(formula: str, sets: list[list[int]]) -> list[int]:
    universe = list(set(item for subset in sets for item in subset))
    alphabets = [char for char in formula if char.isalpha()]
    variables = {i: s for i, s in zip(alphabets, sets)}
    stack = []
    try:
        for token in formula:
            if token.isalpha():
                stack.append(variables[token])
            elif token == '!':
                operand = stack.pop()
                stack.append([item for item in universe if item not in operand])
            elif token in "&|^=>":
                right = stack.pop()
                left = stack.pop()
                if token in "=>": # A ⇒ B = ¬A ∪ B    # A ⇔ B = (A ⇒ B) ∩ (B ⇒ A)
                    stack.append(OPERATORS[token](left, right, universe))
                else:
                    stack.append(OPERATORS[token](left, right))
            else:
                raise ValueError(f"Unknown symbol: {token}")
        
        if len(stack) != 1:
            raise ValueError("Invalid formula: extra operands remaining")
        return stack[0]
    except Exception as e:
        print("Error: ", e)



def main():
    # sets = [[0], [0, 1, 2]]
    sets = [[0], [0], [0]]

    formula = input("Enter a propositional formula in RPN: ")  # e.g., "AB&", "A!", "AB>", "AB&C!^"
    try:
        result = eval_set(formula, sets)
        print("Resulting set:", sorted(result))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()





