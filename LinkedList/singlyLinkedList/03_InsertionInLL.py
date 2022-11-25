class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def traversalOfLL (self):
        temp = self.head
        while (temp):
            print (temp.data, end = " -> ")
            temp = temp.next
            if temp == None:
                print ("None")

    # Step 1 & 2: Allocate the Node & Insert data
    # Step 3 : Make next of new node as head
    # Step 4 : Moving the head to point the new node

    # Complexity Analysis:
    # Time Complexity: O(1), We have a pointer to the head and we can directly attach a node and change the pointer. 
    #                     So the Time complexity of inserting a node at the head position is O(1) as it does a constant amount of work.
    # Auxiliary Space: O(1)

    def insertingNodeToFront (self, newData):
        newNode = Node (newData)
        newNode.next = self.head
        self.head = newNode

    # 1. Check if the given previous node actually exists
    # 2. Create New Node 
    # 3. Make the next of the new node as the previous node's next
    # 4. Make point the next of the previous node to the new node
    # These operations are performed with O(1) time and space complexity

    def insertAfterSpecifiedNode (self, prevNode, newData):
        if prevNode == None:
            return

        newNode = Node (newData)
        newNode.next = prevNode.next
        prevNode.next = newNode

    # 1, 2, 3. Creation of the new node by inserting the data and setting the next as None 
    # 4. If the Linked List is empty make the new node as the head 
    # 5. If elements are present then traverse the linked list till end 
    # 6. Assign the new node to the next of last node 
    # The time complexity is O(N) and space complexity is O(1)

    def insertingNodeAtEnd (self, newData):
        newNode = Node (newData)
        
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = newNode
    

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertingNodeAtEnd (6)
    ll.insertingNodeToFront (7)
    ll.insertingNodeToFront (1)
    ll.insertingNodeAtEnd (4)
    ll.insertAfterSpecifiedNode (ll.head.next, 8)
    ll.traversalOfLL ()
    