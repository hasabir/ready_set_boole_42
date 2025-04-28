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


    def nnf(self, formula_tree):
        if formula_tree is None:
            return
        # node = formula_tree.data
        print("node = ", formula_tree.data)
        for node_char in formula_tree.data:
            if node_char in "|&":
                ...
        if any(node_char in "|&" for node_char in  formula_tree.data):
            while formula_tree.data[-1] == '!':
                self.is_negative ^= True
                print(f"\nnode[-1]: {formula_tree.data[-1]} | is negatif: {self.is_negative}")

                formula_tree.update_data(formula_tree.data[:-1])

            formula_tree.update_data(('&' if formula_tree.data == '|' else '|') if self.is_negative else formula_tree.data)
        elif '!' not in formula_tree.data:
            print("there is not !")
            formula_tree.update_data(f"{formula_tree.data}!" if self.is_negative else formula_tree.data)
        else:
            print("there is ! proceding to remove it")
            formula_tree.update_data(formula_tree.data[:-1] if self.is_negative else formula_tree.data)
        # print(formula_tree.data, end='')
        self.nnf(formula_tree.left)
        self.nnf(formula_tree.right)
        return  formula_tree

    def collect_nodes(self, formula_tree):
        if formula_tree is None:
            return
        self.nnf(formula_tree.left)
        self.nnf(formula_tree.right)
        print(formula_tree.data, end='')


def negation_normal_form(formula: str) -> str:
    try:
        nnf = NegationNormalForm(formula)
        formula_tree = nnf.pars_formula(formula)
        formula_tree.display()
        formula_tree = nnf.nnf(formula_tree)
        formula_tree.display()

        print('\n********************************************\n')

        # nnf.collect_nodes(formula_tree)
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
