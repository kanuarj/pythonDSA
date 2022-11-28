# Time complexity: O(n) where n is no number of nodes
# Auxiliary Space: O(n) size of queue

class Tree:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraversal (temp):
    if not temp:
        return
    inorderTraversal (temp.left)
    print (temp.data, end = ' ')
    inorderTraversal (temp.right)

def deleteDeepestNode (root, deleteNode):
    queue = list ()
    queue.append (root)
    while (len (queue)):
        temp = queue.pop(0)

        if temp is deleteNode:
            temp = None
            return
        
        if temp.right:
            if temp.right is deleteNode:
                temp.right = None
                return
            else:
                queue.append (temp.right)
        
        if temp.left:
            if temp.left is deleteNode:
                temp.left = None
                return
            else:
                queue.append (temp.left)

def deleteElement (root, key):
    if root == None:
        return None
    
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    
    keyNode = None
    queue = list ()
    queue.append (root)
    temp = None

    while (len (queue)):
        temp = queue.pop (0)

        if temp.data == key:
            keyNode = temp
        if temp.left:
            queue.append (temp.left)
        if temp.right:
            queue.append (temp.right)

    if keyNode:
        x = temp.data
        deleteDeepestNode (root, temp)
        keyNode.data = x

    return root

# Important Note:
# The above code will not work if the node to be deleted is the deepest node itself because after
# the function deleteDeepest(root, temp) completes execution,
# the key_node gets deleted(as here key_node is equal to temp)and
# after which replacing key_node‘s data with the deepest node’s data(temp‘s data)
# throws a runtime error.

# To avoid the above error and also to avoid doing BFS twice
# (1st iteration while searching the rightmost deepest node, and 2nd while deleting the rightmost deepest node),
# we can store the parent node while first traversal and after setting the rightmost deepest node’s data to the node needed deletion,
# easily delete the rightmost deepest node.

def deletion (root, key):
    if (root == None):
        return None
    if root.left == None and root.right == None:
        if root.data == None:
            return None
        else:
            return root
    
    keyNode = temp = last = None
    queue = list ()
    queue.append (root)
    while (len (queue)):
        temp = queue.pop (0)
        if temp.data == key:
            keyNode = temp
        
        if temp.left:
            # Preservation of the root node 
            last = temp
            queue.append (temp.left)

        if temp.right:
            last = temp
            queue.append (temp.right)

    if keyNode != None:
        # Replacing the key node to deepest node 
        keyNode.data = temp.data
        if last.right == temp:
            last.right = None
        else:
            last.left = None

    return root

# if __name__ == '__main__':
#     root = Tree (10)
#     root.left = Tree(11)
#     root.left.left = Tree(7)
#     root.left.right = Tree(12)
#     root.right = Tree(9)
#     root.right.left = Tree(15)
#     root.right.right = Tree(8)
#     print(f'The tree before deletion of the prescribed key is ')
#     inorderTraversal (root)
#     key = 11
#     root = deleteElement (root, key)
#     print()
#     print(f'The tree after deletion of {key} element is ')
#     inorderTraversal (root)

if __name__ == '__main__':
    root = Tree (9)
    root.left = Tree (2)
    root.left.left = Tree (4)
    root.left.right = Tree (7)
    root.right = Tree (8)
    print("Inorder traversal before deletion : ", end="")
    inorderTraversal (root)
    key = 7
    root = deletion (root, key)
    print()
    print("Inorder traversal after deletion : ", end="")
    inorderTraversal (root)

# Time complexity: O(n) where n is no number of nodes
# Auxiliary Space: O(n) size of queue