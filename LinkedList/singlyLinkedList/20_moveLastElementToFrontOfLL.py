# Move last element to front of a given Linked List

# Examples:
# Input: 1->2->3->4->5
# Output: 5->1->2->3->4

# Input: 3->8->1->5->7->12
# Output: 12->3->8->1->5->7  

# Approach:
#  Traverse the list till the last node and use two pointers
#     One to store the address of the last node and other for the address of the second last node.
#     After the end of loop, make the second last node as the last node and the last node as the head node

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
    
    def insert (self, new):
        newNode = Node (new)
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

    # Traverse the linked list till the last node and Initialize two pointers to store the address of the last and the second last node
    # Then follow these three steps to move the last node to the front
    #     Make second last as last (secLast->next = NULL). 
    #     Set next of last as head (last->next = *head_ref). 
    #     Make last as head ( *head_ref = last)

    def moveToFront (self):
        last, secondLast = self.head, None
        if not last or not last.next:
            return

        while last and last.next:
            secondLast = last
            last = last.next

        secondLast.next = None

        last.next = self.head
        self.head = last
    
    # Time Complexity: O(N), As we need to traverse the list once.
    # Auxiliary Space: O(1), As constant extra space is used.

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert (1)
    ll.insert (2)
    ll.insert (3)
    ll.insert (4)
    ll.insert (5)
    ll.traversal ()
    ll.moveToFront ()
    ll.traversal ()
        