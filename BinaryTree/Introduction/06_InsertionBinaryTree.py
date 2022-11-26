class Tree:
    def __init__ (self, key):
        self.left = None
        self.right = None
        self.root = key

def inorderTraversal (temp):
    if not temp:
        return

    if temp:
        inorderTraversal (temp.left)
        print (temp.root, end = " ")
        inorderTraversal (temp.right)

# Level order traversal for insertion is used in the binary tree 
def insert (temp, key):
    if not temp:
        root = Tree (key)
        return

    q = list()
    q.append (temp)

    while (len(q)):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Tree (key)
            break
        else:
            q.append (temp.left)

        if not temp.right:
            temp.right = Tree (key)
            break
        else:
            q.append (temp.right)

if __name__ == '__main__':
    root = Tree(10)
    root.left = Tree(11)
    root.left.left = Tree(7)
    root.right = Tree(9)
    root.right.left = Tree(15)
    root.right.right = Tree(8)
 
    print("Inorder traversal before insertion:", end = " ")
    inorderTraversal(root)
 
    key = 12
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorderTraversal(root)