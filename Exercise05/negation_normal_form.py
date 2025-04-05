from node import Node

OPERATORS = {
    "^": lambda A, B: f"{A}{B}!&{A}!{B}&|",
    ">": lambda A, B: f"{A}!{B}|",
    "=": lambda A, B: f"{A}{B}&{A}!{B}!&|",
}


def pars_formula(formula):
    try:
        if formula[-1] == '!':
            formula = formula[:-1]
        for i in formula:
            if i not in "&!|^>=" and (not i.isalpha() or i.lower() == i):
                raise SyntaxError(f"Syntax error")
        stack = []
        for i in formula:
            if i.isalpha():
                stack.append(Node(i))
            elif i in "|&":
                node = Node(i)
                node.right, node.left= stack.pop(), stack.pop()
                stack.append(node)
            elif i == '!':
                stock = stack.pop()
                stock.update_data(f"{stock.data}!")
                stack.append(stock)
            elif i in  "=>^":
                B = stack.pop().data
                A = stack.pop().data
                stack.append(pars_formula(OPERATORS[i](A, B)))
        if len(stack) != 1:
            raise ValueError("Invalid formula")
    except Exception as e:
        raise e
    return stack.pop()        


def collect_nodes(formula_tree, is_negative):
    if formula_tree is None:
        return
    collect_nodes(formula_tree.left, is_negative)
    collect_nodes(formula_tree.right, is_negative)
    node = formula_tree.data
    
    if node in "|&":
        node = ('&' if node == '|' else '|') if is_negative else node
    elif '!' not in node:
        node = f"{node}!" if is_negative else node
    else:
        node = node[:-1] if is_negative else node
        
    print(node, end='')

            
def negation_normal_form(formula: str) -> str:
    try:
        formula_tree = pars_formula(formula)
        formula_tree.display()
        print('\n********************************************\n')
        is_negative = False
        if formula[-1] == '!':
            is_negative = True
        collect_nodes(formula_tree, is_negative)
        print()
    except Exception as e:
        raise e
    
    
    
    

            
def main():
    try:
        formula = input("Enter a boolean formula: ")
        negation_normal_form(formula)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
