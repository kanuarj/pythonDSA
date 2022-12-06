class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert (self, newData):
        newNode = Node (newData)
        newNode.next = self.head
        self.head = newNode

    def insertInEnd (self, newData):
        newNode = Node (newData)
        if self.head is None:
            self.head = newNode
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = newNode

    def traversal (self):
        temp = self.head
        while temp:
            print (temp.data, end = ' -> ')
            temp = temp.next
            if temp is None:
                print ("None")

    # Search an element in a Linked List (Iterative Approach): 
    # Follow the below steps to solve the problem:

    # Initialize a node pointer, current = head.
    # Do following while current is not NULL
    #     If the current value (i.e., current->key) is equal to the key being searched return true.
    #     Otherwise, move to the next node (current = current->next).
    # If the key is not found, return false 

    def searchIterative (self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                return True
            current = current.next
        return False

    # Time Complexity: O(N), Where N is the number of nodes in the LinkedList
    # Auxiliary Space: O(1)

    # -----------------------------------------------------------------------------------------------

    # Search an element in a Linked List (Recursive Approach): 
    # Follow the below steps to solve the problem:
    # If the head is NULL, return false.
    # If the head’s key is the same as X, return true;
    # Else recursively search in the next node. 

    def searchRecursive (self, node, x):
        if not node:
            return False
        if node.data is x:
            return True
        return self.searchRecursive (node.next, x)

    def searchRecursiveWrapper (self, x):
        return self.searchRecursive (self.head, x)

    # Time Complexity: O(N)
    # Auxiliary Space: O(N), Stack space used by recursive calls

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert (1)
    ll.insert (2)
    ll.traversal ()
    ll.insertInEnd (3)
    ll.traversal ()
    # if ll.searchIterative (4):
    #     print ('The element is present')
    # else:
    #     print ('The element is not present')

    if ll.searchRecursiveWrapper (3):
        print ('The element is present')
    else:
        print ('The element is not present')