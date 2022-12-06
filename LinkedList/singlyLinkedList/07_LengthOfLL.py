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

    def insertInEnd (self, newData):
        newNode = Node (newData)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def traversalOfLL (self):
        temp = self.head
        while temp:
            print (temp.data, end = ' -> ')
            temp = temp.next
            if temp == None:
                print ("None")

    # An iterative approach for finding the length of the linked list:
    # Follow the given steps to solve the problem:
    # Initialize count as 0 
    # Initialize a node pointer, current = head.
    # Do following while current is not NULL
    #   current = current -> next
    #   Increment count by 1.
    # Return count 

    def lengthOfLL (self):
        currentNode = self.head
        countOfLength = 0
        while (currentNode):
            countOfLength += 1
            currentNode = currentNode.next
        return countOfLength
    
    # Time complexity: O(N), Where N is the size of the linked list
    # Auxiliary Space: O(1), As constant extra space is used.

    # -------------------------------------------------------------------

    # A recursive approach for finding the length of the linked list:
    # Follow the given steps to solve the problem:
    #     If the head is NULL, return 0.
    #     Otherwise, return 1 + getCount(head->next) 

    def lengthRecursiveLL (self, headNode):
        if not headNode:
            return 0
        else:
            return 1 + self.lengthRecursiveLL (headNode.next)

    def recursiveLL (self):
        return self.lengthRecursiveLL (self.head)
    
    # Time Complexity: O(N), As we are traversing the linked list only once.
    # Auxiliary Space: O(N), Extra space is used in the recursion call stack.

    # -------------------------------------------------------------------------

    # Recursive approach for finding the length of the linked list using constant space:
    # To solve the problem follow the below idea:
    # The above recursive approach can be modified to make it a tail recursive function and thus our auxiliary space will become O(1)

    def spaceEfficientRecursiveLengthLL (self, headNode, count = 0):
        if not headNode:
            return 0
        else:
            return 1 + self.spaceEfficientRecursiveLengthLL (headNode.next, count+1)

    def spaceEffRecLenLLWrapper (self):
        return self.spaceEfficientRecursiveLengthLL (self.head)

    # Time Complexity: O(N), As we are traversing the list only once.
    # Auxiliary Space: O(1), As we are using the tail recursive function, no extra space is used in the function call stack

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert (1)
    ll.insert (2)
    ll.insert (3)
    ll.insertInEnd (4)
    ll.traversalOfLL ()
    # print (f'The length of the Linked List is {ll.lengthOfLL ()}')
    # print (f'The length of the Linked List is {ll.recursiveLL ()}')
    print (f'The length of the Linked List is {ll.spaceEffRecLenLLWrapper ()}')
