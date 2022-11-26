# Complexity Analysis : 
# Best Case : O(1) if given position is 1 
# Average  & Worst Case : O(N)  if position given is size-1 then need to traverse till position not found.
# Space Complexity : O(1) no extra any space is required

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
            if (temp == None):
                print ("None")

    def insertNode (self, newData):
        newNode = Node (newData)
        newNode.next = self.head
        self.head = newNode

    def deleteNodeAtSpecificPosition (self, key):
        if self.head is None:
            return

        index = 0
        current = self.head
        while current.next and index < key:
            previous = current
            current = current.next
            index += 1

        if index < key:
            print ("Index is not in range")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next


if __name__ == '__main__':
    ll = LinkedList ()
    ll.head = Node (1)
    second = Node (2)
    third = Node (3)
    ll.head.next = second
    second.next = third
    ll.traversal ()
    ll.deleteNodeAtSpecificPosition (2)
    ll.traversal ()