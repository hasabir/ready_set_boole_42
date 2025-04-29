import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from utilities.node import Node

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


    def pars_formula(self, formula):
        try:
            for i in formula:
                if i not in "&!|^>=" and (not i.isalpha() or i.lower() == i):
                    raise SyntaxError(f"Syntax error")
            stack = []
            for i in formula:
                if i == '!':
                    stock = stack.pop()
                    stack.append(f"{stock}!")
                elif i in  self.operators:
                    B = stack.pop()
                    A = stack.pop()
                    stack.append(self.operators[i](A, B))
                else:
                    stack.append(i)
            return "".join(stack)
        except Exception as e:
            raise e

    def build_tree(self, formula):
        try:
            stack = []
            for stok in formula:
                if stok.isalpha():
                    stack.append(Node(stok))
                elif stok == '!':
                    child = stack.pop()
                    node = Node('!')
                    node.left = child
                    stack.append(node)
                elif stok in ('&', '|'):
                    b = stack.pop()
                    a = stack.pop()
                    node = Node(stok)
                    node.left, node.right = a, b
                    stack.append(node)
                else:
                    raise SyntaxError(f"Unknown token")
            if len(stack) != 1:
                raise ValueError("Malformed formula during tree build")
            return stack[0]
        except Exception as e:
            raise e


    def collect_nodes(self, formula_tree, is_negative=False):
        if formula_tree is None:
            return None

        if formula_tree.data == '!':
            return self.collect_nodes(formula_tree.left, not is_negative)

        self.collect_nodes(formula_tree.left, is_negative)
        self.collect_nodes(formula_tree.right, is_negative)

        node_data = formula_tree.data
        if node_data in "|&":
            if is_negative:
                node_data = '&' if node_data == '|' else '|'
        else:
            if is_negative:
                node_data += '!'
        
        print(node_data, end='')


def negation_normal_form(formula: str) -> str:
    try:
        nnf = NegationNormalForm(formula)
        formula = nnf.pars_formula(formula)
        formula_tree = nnf.build_tree(formula)
        # formula_tree.display()
        print('\n********************************************\n')


        nnf.collect_nodes(formula_tree)
        print()
    except Exception as e:
        raise e
    
            
def main():
    try:
        formula = input("Enter the formula: ")
        negation_normal_form(formula)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
