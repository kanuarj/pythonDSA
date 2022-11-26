class Tree:
    def __init__ (self, key):
        self.left = None
        self.right = None
        self.root = key

# Inorder Traversal : Left Node, Root, Right Node 
# Time Complexity: O(N)
# Auxiliary Space: If we don’t consider the size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree. 
def inorderTraversal (root):
    if root:
        inorderTraversal (root.left)
        print (root.root, end = " ")
        inorderTraversal (root.right)

# Preorder Traversal : Root, Left Node, Right Node 
def preorderTraversal (root):
    if root:
        print (root.root, end = " ")
        preorderTraversal (root.left)
        preorderTraversal (root.right)

# Postorder Traversal : Left Node, Right Node, Root 
def postorderTraversal (root):
    if root:
        postorderTraversal (root.left)
        postorderTraversal (root.right)
        print (root.root, end = " ")

if __name__ == '__main__':
    root = Tree (1)
    root.left = Tree (2)
    root.right = Tree (3)
    root.left.left = Tree (4)
    root.left.right = Tree (5)
    inorderTraversal (root)
    print ()
    preorderTraversal (root)
    print ()
    postorderTraversal (root)

