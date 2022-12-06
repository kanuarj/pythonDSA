# Find the middle of a given linked list

# Given a singly linked list, find the middle of the linked list.
# For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
# If there are even nodes, then there would be two middle nodes, we need to print the second middle element.
# For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4. 

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

    # Method 1: Traverse the whole linked list and count the no. of nodes.
    #     Now traverse the list again till count/2 and return the node at count/2

    def lengthOfLL (self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        return length
    
    def middleElement (self):
        temp = self.head
        if temp is not None:
            length = self.lengthOfLL ()
            middle = length // 2
            while middle is not 0:
                temp = temp.next
                middle -= 1
            print (f'The middle term is {temp.data}')

    # Time Complexity: O(n) where n is no of nodes in linked list
    # Auxiliary Space: O(1)

    # ------------------------------------------------------------------------------------------------------

    # Method 2: Traverse linked list using two-pointers. Move one pointer by one and the other pointers by two.
    #     When the fast pointer reaches the end, the slow pointer will reach the middle of the linked list.

    def middleElementTwoPointers (self):
        first = second = self.head
        while second and second.next:
            first = first.next
            second = second.next.next
        print (f'The middle element is {first.data}')

    # Time Complexity: O(N), As we are traversing the list only once.
    # Auxiliary Space: O(1), As constant extra space is used.

    # -------------------------------------------------------------------------------------------------------

    # Method 3: Initialize the mid element as head and initialize a counter as 0.
    #     Traverse the list from the head, while traversing increment the counter and change mid to mid->next whenever the counter is odd.
    #     So the mid will move only half of the total length of the list. 

    def middleElementMidHead (self):
        count = 0
        middle = head = self.head
        while head is not None:
            if count & 1:
                middle = middle.next
            count += 1
            head = head.next
        print (f'The element in the middle is {middle.data}')

    # Time Complexity: O(N), As we are traversing the list once.
    # Auxiliary Space: O(1), As constant extra space is used.

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insert (1)
    ll.insertInEnd (2)
    ll.insertInEnd (3)
    ll.insertInEnd (4)
    ll.traversal ()
    # ll.middleElement ()
    # ll.middleElementTwoPointers ()
    ll.middleElementMidHead ()