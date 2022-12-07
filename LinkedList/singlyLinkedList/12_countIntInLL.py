# Write a function that counts the number of times a given int occurs in a Linked List

# Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.
# For example, if the given linked list is 1->2->1->2->1->3->1 and the given key is 1, then the output should be 4.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertion (self, newData):
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

    # Algorithm:  
    # Step 1: Start
    # Step 2: Create A Function Of A Linked List, Pass A Number 
    #         As Arguments And Provide The Count Of The Number To The Function.
    # Step 3: Initialize Count Equal To 0.
    # Step 4: Traverse In Linked List Until Equal Number Found.
    # Step 5: If Found A Number Equal To Update Count By 1.
    # Step 6: After Reaching The End Of The Linked List Return Count.
    # Step 7: Call The Function.
    # Step 8: Prints The Number Of Int Occurrences.
    # Step 9: Stop.

    def countIterative (self, key):
        current, count = self.head, 0
        while current is not None:
            if current.data == key:
                count += 1
            current = current.next
        return count

    # Time Complexity: O(n) 
    # Auxiliary Space: O(1)
    # ------------------------------------------------------------------------------------
    # Algorithm
    #     count(head, key);
    #     if head is NULL
    #     return frequency
    #     if(head->data==key)
    #     increase frequency by 1
    #     count(head->next, key)
    def countRecursive (self, head, key, count):
        if not head:
            return count
        if head.data == key:
            count += 1
        return self.countRecursive (head.next, key, count)

    def countWrapper (self, key):
        return self.countRecursive (self.head, key, count=0)

    # Time complexity: O(n) where n is size of linked list
    # Auxiliary Space: O(n) for call stack since using recursion 


if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertion (1)
    ll.insertion (2)
    ll.insertion (3)
    ll.insertion (3)
    ll.traversal ()
    # print (f'The occurence of element in given LL is {ll.countIterative (3)}')
    print (f'The occurence of element in given LL is {ll.countWrapper (55)}')