OPERATORS = {
    "&": lambda x, y: x & y,
    "|": lambda x, y: x | y,
    "^": lambda x, y: x ^ y,
}

def eval_set(formula: str, sets: list[set[int]]) -> set[int]:
    universe = set().union(*sets)
    alphabets = [char for char in formula if char.isalpha()]
    variables = {i: s for i, s in zip(alphabets, sets)}
    stack = []

    try:
        for token in formula:
            if token.isalpha():
                stack.append(variables[token])
            elif token == '!':
                operand = stack.pop()
                stack.append(universe - operand)
            elif token in "&|^":
                right = stack.pop()
                left = stack.pop()
                stack.append(OPERATORS[token](left, right))
            elif token == '>':  # A ⇒ B = ¬A ∪ B
                right = stack.pop()
                left = stack.pop()
                stack.append((universe - left) | right)
            elif token == '=':  # A ⇔ B = (A ∩ B) ∪ (¬A ∩ ¬B)
                right = stack.pop()
                left = stack.pop()
                stack.append((left & right) | ((universe - left) & (universe - right)))
            else:
                raise ValueError(f"Unknown symbol: {token}")
        
        if len(stack) != 1:
            raise ValueError("Invalid formula: extra operands remaining")
        return stack[0]
    except Exception as e:
        print("Error: ", e)



def main():
    sets = [
        {0, 1, 2},
        {2, 3, 4},
        {5, 6, 7},
    ]
    formula = input("Enter a propositional formula in RPN: ")  # e.g., "AB&", "A!", "AB>", "AB&C!^"
    try:
        result = eval_set(formula, sets)
        print("Resulting set:", sorted(result))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()





