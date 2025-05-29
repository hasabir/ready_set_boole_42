import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from Exercise04.truth_table import print_truth_table
from utilities.node import Node
from Exercise05.negation_normal_form import NegationNormalForm , negation_normal_form


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
        formula = negation_normal_form(formula)
        cnf = ConjunctiveNormalForm(formula)
        formula_tree = cnf.build_tree(cnf.pars_formula(formula))
        formula_tree.display()
        formula_tree = cnf.distribute_or_over_ands(formula_tree)
        formula_tree.display()
        return(cnf.get_result(formula_tree))
    except Exception as e:
        raise e




def main():
    try:
        formula = input("Enter a boolean formula: ")
        # print("Conjunctive Normal Form:", conjunctive_normal_form(formula))
        print_truth_table(formula)
        result = conjunctive_normal_form(formula)
        print("result: ",result)
        print('\n********************************************\n')
        print_truth_table(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
