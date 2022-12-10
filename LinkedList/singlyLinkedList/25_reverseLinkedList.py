class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
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

    # Reverse a linked list by Iterative Method:
    # The idea is to use three pointers curr, prev, and next to keep track of nodes to update reverse links.
    # Implementation :
    # Initialize three pointers prev as NULL, curr as head, and next as NULL.
    # Iterate through the linked list. In a loop, do the following:
    #     Before changing the next of curr, store the next node 
    #         next = curr -> next
    #     Now update the next pointer of curr to the prev 
    #         curr -> next = prev 
    #     Update prev as curr and curr as next 
    #         prev = curr 
    #         curr = next

    def reverse (self):
        prev, current = None, self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Time Complexity: O(N), Traversing over the linked list of size N. 
    # Auxiliary Space: O(1)

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert (3)
    ll.insert (2)
    ll.insert (1)
    ll.traversal ()
    ll.reverse ()
    ll.traversal ()