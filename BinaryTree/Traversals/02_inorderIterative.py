# Time Complexity: O(n)
# Space Complexity: O(n)

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraversal (root):
    current = root
    stack = list ()
    while True:
        if current is not None:
            stack.append (current)
            current = current.left
        elif stack:
            current = stack.pop ()
            print (current.data, end = ' ')
            current = current.right
        else:
            break
    print ()

if __name__ == '__main__':
    root = Tree (1)
    root.left = Tree (2)
    root.right = Tree (3)
    root.left.left = Tree (4)
    root.left.right = Tree (5)
    inorderTraversal (root)