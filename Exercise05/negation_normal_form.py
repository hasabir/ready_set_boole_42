import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from node import Node

class NegationNormalForm:
    def __init__(self, formula: str):
        self.formula = formula
        self.formula_tree = None
        self.is_negative = False
        self.operators = {
            "^": lambda A, B: f"{A}{B}!&{A}!{B}&|",
            ">": lambda A, B: f"{A}!{B}|",
            "=": lambda A, B: f"{A}{B}&{A}!{B}!&|",
        }

    def pars_formula(self):
        try:
            if self.formula[-1] == '!':
                self.is_negative = True
                self.formula = self.formula[:-1]
            for i in self.formula:
                if i not in "&!|^>=" and (not i.isalpha() or i.lower() == i):
                    raise SyntaxError(f"Syntax error")
            stack = []
            for i in self.formula:
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
                    stack.append(self.pars_formula(self.operators[i](A, B)))
            if len(stack) != 1:
                raise ValueError("Invalid formula")
        except Exception as e:
            raise e
        self.formula_tree = stack.pop()
        return self.formula_tree


    def collect_nodes(self, formula_tree):
        if formula_tree is None:
            return
        self.collect_nodes(formula_tree.left)
        self.collect_nodes(formula_tree.right)
        node = formula_tree.data
        
        if node in "|&":
            node = ('&' if node == '|' else '|') if self.is_negative else node
        elif '!' not in node:
            node = f"{node}!" if self.is_negative else node
        else:
            node = node[:-1] if self.is_negative else node
            
        print(node, end='')

            
def negation_normal_form(formula: str) -> str:
    try:
        nnf = NegationNormalForm(formula)
        formula_tree = nnf.pars_formula()
        formula_tree.display()
        print('\n********************************************\n')

        nnf.collect_nodes()
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
