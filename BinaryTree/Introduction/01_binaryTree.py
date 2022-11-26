# Representation of Binary Tree:
# Each node in the tree contains the following:
# - Data
# - Pointer to the left child
# - Pointer to the right child

class Tree:
    def __init__ (self, key):
        self.left = None
        self.right = None
        self.root = key

if __name__ == '__main__':
    root = Tree (1)
    root.left = Tree (2)
    root.right = Tree (3)
    root.left.left = Tree (4)

#     1
#     /\
#    2  3
#   /
#   4 
