class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
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

    # Naive Approach:
    #     Calculate the length of the Linked List. Let the length be len. 
    #     Print the (len – n + 1)th node from the beginning of the Linked List. 

    def nthNodeFromEnd (self, n):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        
        if length < n:
            print ('The given index is not present in the Linked List')
            return
        
        temp = self.head
        counter = 0
        while counter == (length-n):
            temp = temp.next
            counter += 1
        print (temp.data)

    # Time complexity: O(M) where M is the size of the linked list
    # Auxiliary Space: O(1)

    # ---------------------------------------------------------------------------------------------
    
    # Nth node from the end of a Linked List using two pointers:
    #     Maintain two pointers main_ptr and ref_ptr
    #     Move ref_ptr to the Nth node from the start
    #     Now move both main_ptr and ref_ptr, until the ref_ptr reaches the last node
    #     Now print the data of the main_ptr, as it is at the Nth node from the end

    def nthNodeFromEndTwoPointers (self, n):
        mainPointer = referencePointer = self.head
        count = 0
        if (self.head is not None):
            while count < n:
                if referencePointer is None:
                    print ('The given index value is more than length of linked list')
                    return
                referencePointer = referencePointer.next
                count += 1
        
        if referencePointer is None:
            self.head = self.head.next
            if self.head is not None:
                print (f'The data from {n} index is {mainPointer.data}')
            else:
                while referencePointer is not None:
                    mainPointer = mainPointer.next
                    referencePointer = referencePointer.next
                print (f'The data from {n} index is {mainPointer.data}')

    # Time Complexity: O(M) where M is the length of the linked list.
    # Auxiliary Space: O(1)

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert (1)
    ll.insertInEnd (2)
    ll.insertInEnd (3)
    ll.traversal ()
    # ll.nthNodeFromEnd (3)
    ll.nthNodeFromEndTwoPointers (5)