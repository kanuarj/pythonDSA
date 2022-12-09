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

    
if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertInEnd (1)
    ll.insertInEnd (2)
    ll.insertInEnd (3)
    ll.traversal ()
    ll.swapNodes (2, 3)
    ll.traversal ()