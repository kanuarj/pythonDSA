# Swap nodes in a linked list without swapping data

# Given a linked list and two keys in it, swap nodes for two given keys.
# Nodes should be swapped by changing links.
# Swapping data of nodes may be expensive in many situations when data contains many fields.
# It may be assumed that all keys in the linked list are distinct.

# Examples: 
# Input: 10->15->12->13->20->14,  x = 12, y = 20
# Output: 10->15->20->13->12->14

# Input: 10->15->12->13->20->14,  x = 10, y = 20
# Output: 20->15->12->13->10->14

# Input: 10->15->12->13->20->14,  x = 12, y = 13
# Output: 10->15->13->12->20->14

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
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
                print ('None')

    # Naive Approach:
    # The idea is to first search x and y in the given linked list. If any of them is not present, then return.
    # While searching for x and y, keep track of current and previous pointers.
    # First change next of previous pointers, then change next of current pointers.
    def swapNodes (self, x, y):
        if x == y:
            return
        prevX, currentX = None, self.head
        while currentX is not None and currentX.data is not x:
            prevX = currentX
            currentX = currentX.next

        prevY, currentY = None, self.head
        while currentY is not None and currentY.data is not y:
            prevY = currentY
            currentY = currentY.next

        if currentX is None or currentY is None:
            return

        if prevX != None:
            prevX.next = currentY
        else:
            self.head = currentY

        if prevY != None:
            prevY.next = currentX
        else:
            self.head = currentX

        temp = currentX.next
        currentX.next = currentY.next
        currentY.next = temp

    # Time Complexity: O(N)
    # Auxiliary Space: O(1) 
    # ====================================================================================
    # Optimized solution using single traversal
    def swapNodesOptimized (self, x, y):
        if x == y:
            return None
        temp = self.head
        first = second = None
        while temp.next is not None:
            if temp.next.data == x:
                first = temp
            elif temp.next.data == y:
                second = temp
            temp = temp.next

        if first is not None and second is not None:
            temp = first.next
            first.next = second.next
            second.next = temp
            temp = first.next.next
            first.next.next = second.next.next
            second.next.next = temp
    
    # Time complexity: O(N)
    # Auxiliary Space: O(1)

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertInEnd (1)
    ll.insertInEnd (2)
    ll.insertInEnd (3)
    ll.traversal ()
    ll.swapNodesOptimized (2, 3)
    ll.traversal ()