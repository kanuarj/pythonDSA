class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    def insert (self, newData):
        newNode = Node (newData)
        newNode.next = self.head
        self.head = newNode

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

    # Check if a Singly Linked List is Palindrome using Stack:
    # A simple solution is to use a stack of list nodes. This mainly involves three steps.
    # Traverse the given list from head to tail and push every visited node to stack.
    # Traverse the list again. For every visited node, pop a node from the stack and compare data of popped node with the currently visited node.
    # If all nodes matched, then return true, else false.
    def palindromeIterative (self):
        current, isPalindrome, stackHolder = self.head, True, list ()
        
        while current is not None:
            stackHolder.append (current.data)
            current = current.next

        while self.head is not None:
            stackElement = stackHolder.pop ()
            if self.head.data == stackElement:
                isPalindrome = True
            else:
                isPalindrome = False
                break
            self.head = self.head.next
        return isPalindrome

    # Time complexity: O(N), Iterating over the linked list of size N.
    # Auxiliary Space: O(N), Using an auxiliary stack


if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert ('R')
    ll.insertInEnd ('A')
    ll.insertInEnd ('D')
    ll.insertInEnd ('A')
    ll.insertInEnd ('R')
    ll.traversal ()
    print (ll.palindromeIterative ())