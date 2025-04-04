# class NegationNormalForm:
#     def __init__(self):
#         ...
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key):
        if self.data == key:
            return
        elif self.data < key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        else:  # self.data > key
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
    
    def update_data(self, data):
        self.data = data
    
    
    # def traverse
        
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2




def pars_formula(formula):
    if formula[-1] == '!':
        formula = formula[:-1]

    stack = []
    for i in formula:
        if i.isalpha():
            stack.append(Node(i))
        elif i in "|&":
            right_childe = stack.pop()
            left_childe = stack.pop()

            node = Node(i)
            node.left = left_childe
            node.right = right_childe
            
            stack.append(node)
        elif i == '!':
            stock = stack.pop()
            stock.update_data(f"{stock.data}!")
            stack.append(stock)
        elif i in  "=>^":
            B = stack.pop().data
            A = stack.pop().data
            if i == '=':
                stack.append(pars_formula(f"{A}{B}&{A}!{B}!&|"))
            elif i == '>':
                stack.append(pars_formula(f"{A}!{B}|"))
            elif i == '^':
                stack.append(pars_formula(f"{A}{B}!&{A}!{B}&|"))
    return stack.pop()        
            
            
def negation_normal_form(formula: str) -> str:
    formula_tree = pars_formula(formula)
    formula_tree.display()
    
    # convert_to_rpn(formula_tree)
    
        







            
def main():
    try:
        formula = input("Enter a boolean formula: ")
        node = negation_normal_form(formula)
        # node.display()

        # print(f"Result: {pars_formula(formula)}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
