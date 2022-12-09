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

    def traversal (self):
        temp = self.head
        while temp:
            print (temp.data, end = ' -> ')
            temp = temp.next
            if temp is None:
                print ('None')

    def insertInEnd (self, newData):
        newNode = Node (newData)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    # Naive Approach: 
    # Use two loops, Outer loop is used to pick the elements one by one and the Inner loop compares the
    # picked element with the rest of the elements. 
    def removeDuplicates (self):
        first = second = duplicate = None
        first = self.head
        while (first != None and first.next != None):
            second = first
            while (second.next != None):
                if first.data == second.next.data:
                    duplicate = second.next
                    second.next = second.next.next
                else:
                    second = second.next
            first = first.next
    
    # Time Complexity: O(N2)
    # Auxiliary Space: O(1)
    # =========================================================================================================
    # More optimal solutions in further files 

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert (1)
    ll.insert (4)
    ll.insert (4)
    ll.insert (4)
    ll.insertInEnd (4)
    ll.traversal ()
    ll.removeDuplicates ()
    ll.traversal ()