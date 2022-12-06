# Write a function to get Nth node in a Linked List

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
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

    # Algorithm: 
    # 1. Initialize count = 0
    # 2. Loop through the link list
    #     a. if the count is equal to the passed index then return the current
    #         node
    #     b. Increment count
    #     c. change current to point to next of the current.

    def getNthIterative (self, index):
        current, count = self.head, 0
        while current:
            if count is index:
                return current.data
            count += 1
            current = current.next
        return -1 

    # Time Complexity: O(n)
    # Auxiliary Space: O(1) space created for variables

    # -------------------------------------------------------------------------------------------

    # Method 2- With Recursion
    # Algorithm :
    # getnth(node,n)
    # 1. Initialize count = 0
    # 2. if count==n
    #     return node->data
    # 3. else
    #     return getnth(node->next,n-1)

    def getNthRecusive (self, head, position):
        count = 0
        if head:
            if count is position:
                print (head.data)
            else:
                return self.getNthRecusive (head.next, position-1)
        else:
            print ('Element does not exist')

    def getNthRecursiveWrapper (self, position):
        return self.getNthRecusive (self.head, position)

    # Time Complexity : O(n) 
    # Auxiliary Space : O(n) due to recursive calls.
    
if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert (11)
    ll.insertInEnd (233)
    ll.insertInEnd (32)
    ll.traversal ()
    # print (ll.getNthIterative (5))
    ll.getNthRecursiveWrapper (2)