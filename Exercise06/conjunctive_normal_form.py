# from node import Node
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from Exercise05.node import Node
from Exercise05.negation_normal_form import NegationNormalForm 


class ConjunctiveNormalForm(NegationNormalForm):
    def __init__(self, formula: str):
        super().__init__(formula)


    def cross_product_disjunction(self, node):
        left = node.left
        right = node.right

        if left.data == '&' and right.data != '&':
            return Node('&',
                left=Node('|', left=left.left, right=right),
                right=Node('|', left=left.right, right=right)
            )
        elif left.data != '&' and right.data == '&':
            return Node('&',
                left=Node('|', left=left, right=right.left),
                right=Node('|', left=left, right=right.right)
            )
        elif left.data == '&' and right.data == '&':
            return Node('&',
                left=Node('&',
                    left=Node('|', left=left.left, right=right.left),
                    right=Node('|', left=left.left, right=right.right)
                ),
                right=Node('&',
                    left=Node('|', left=left.right, right=right.left),
                    right=Node('|', left=left.right, right=right.right)
                )
            )


    def distribute_or_over_ands(self, formula_tree):
        if formula_tree is None:
            return None

        formula_tree.left  = self.distribute_or_over_ands(formula_tree.left)
        formula_tree.right = self.distribute_or_over_ands(formula_tree.right)
        node = formula_tree.data
        
        if formula_tree.data == '|' and (
        (formula_tree.left  and formula_tree.left.data  == '&') or
        (formula_tree.right and formula_tree.right.data == '&')
        ):
            return self.distribute_or_over_ands(self.cross_product_disjunction(formula_tree))
        
        return formula_tree
        

def conjunctive_normal_form(formula: str) -> str:
    try:
        cnf = ConjunctiveNormalForm(formula)
        formula_tree = cnf.pars_formula()
        print('\n********************************************\n')
        formula_tree.display()
        print("\nConjunctive Normal Form:", end=' ')
        formula_tree = cnf.distribute_or_over_ands(formula_tree)
        cnf.collect_nodes(formula_tree)
        
        print('\n********************************************\n')
        formula_tree.display()
        print()
    except Exception as e:
        raise e




def main():
    try:
        formula = input("Enter a boolean formula: ")
        conjunctive_normal_form(formula)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
