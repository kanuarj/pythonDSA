class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def traverseList (self):
        temp = self.head
        while (temp):
            print (temp.data, end = " -> ")
            temp = temp.next
            if temp is None:
                print ("None")

    def insertNodeInFront (self, newData):
        newNode = Node (newData)
        newNode.next = self.head
        self.head = newNode

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list

    def deleteNode (self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if (temp.data == key):
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if (temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertNodeInFront (7)
    ll.insertNodeInFront (1)
    ll.insertNodeInFront (3)
    ll.insertNodeInFront (2)
    ll.traverseList ()
    ll.deleteNode (1)
    ll.traverseList ()