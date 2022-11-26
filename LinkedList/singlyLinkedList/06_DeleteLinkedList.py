# Time Complexity: O(n) 
# Auxiliary Space: O(1)

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal (self):
        temp = self.head
        while temp:
            print (temp.data, end = " -> ")
            temp = temp.next
            if temp is None:
                print ("None")

    def insertNode (self, newData):
        newNode = Node (newData)
        newNode.next = self.head
        self.head = newNode

    def deleteLinkedList (self):
        currentNode = self.head
        while currentNode:
            nextNode = currentNode.next
            del currentNode.data
            currentNode = nextNode

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertNode (10)
    ll.insertNode (20)
    ll.insertNode (30)
    ll.traversal ()
    ll.deleteLinkedList ()
    print ("The Linked List has been successfully deleted")