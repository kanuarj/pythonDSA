# Time Complexity:
# Time Complexity, Worst Case, Average Case
# Search, O(n) ,O(n)
# Insert, O(1), O(1)
# Deletion, O(1), O(1)

# Auxiliary Space: O(N)

# Representation of Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def ___init__ (self):
        self.head = None

    # Linked List Traversal

    def traversalOfLL (self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

if __name__ == '__main__':
    # Construction of Linked List
    ll = LinkedList ()
    ll.head = Node (1)
    second = Node (2)
    third = Node (3)
    ll.head.next = second
    second.next = third
    # Traversal Segment
    ll.traversalOfLL ()