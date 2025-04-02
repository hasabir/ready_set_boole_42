# class NegationNormalForm:
#     def __init__(self):
#         ...

# class Node:
#     def __init__(self, data=None):
#         self.left = None
#         self.right = None
#         self.data = data
    
#     def PrintTree(self):
#         print(self.data)
    
#     def insert(self, data):
#         if self.data:
#             if data and self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data



# def main():
#     tree = Node()
#     # branch = Node()
    
#     tree.insert("A")
#     tree.left = Node("B")
#     tree.right = Node("C")
#     tree.PrintTree()
    
#     print(f"root: {tree.data} left: {tree.left.data} right: {tree.right.data}")
    



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# def material_condition(A, B):
#     '''The Material condition A > B can be represented this way:
#         AB!&|
#     which is equivalent to:
#         !A | B'''
    
#     root = Node("|")
#     root.right = Node(B)
#     root.left = Node(f"{A}!")
#     return root

# def exlusive_or(A, B):
#     '''The exclusive disjunction A ^ q can also be represented this way:
#         AB!&A!B&|    
#     which is equivalent to:
#         (A & !B) | (!A & B) 
#     '''
    
#     root = Node("|")
#     node_right = Node('&')
#     node_left = Node('&')
    
#     node_right.right = Node(B)
#     node_right.left = Node(f"{A}!")

#     node_left.right = Node(f"{B}!")
#     node_left.left = Node(A)
    
#     root.right = node_right
#     root.left = node_left


# def Logical_equivalence(A, B): 
#     '''The logical equivalence A = B can be represented this way:
#         AB&A!B!&|
#     which is equivalent to:
#         (A & B) | (!A & !B) 
#     '''






def negation_normal_form(formula: str) -> str:
    is_negation = False
    # tree = Node()
    # for i in formula[::-1]:
    #     if i == '!':
    #         is_negation = True
    #     else:
            
def main():
    ...


if __name__ == "__main__":
    main()