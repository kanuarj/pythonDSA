# Remove duplicates from a sorted linked list

# Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once. 
# For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def deletionOfNode (self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    # Algorithm: Traverse the list from the head (or start) node. While traversing, compare each node with its next node.
    # If the data of the next node is the same as the current node then delete the next node.
    # Before we delete a node, we need to store the next pointer of the node 
    def removeDuplicates (self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
    # Time Complexity: O(n) where n is the number of nodes in the given linked list.
    # Space Complexity: O(1) , as there is no extra space used.
    # =====================================================================================================================
    def removeDupilicatesRecursive (self, head):
        if head is None:
            return
        if head.next is not None:
            if head.data == head.next.data:
                # holder =  head.next
                head.next = head.next.next
                self.removeDupilicatesRecursive (head)
            else:
                self.removeDupilicatesRecursive (head.next)
        return head

    def removeDupilicatesRecursiveWrapper (self):
        return self.removeDupilicatesRecursive (self.head)

    # Time Complexity: O(n) where n is the number of nodes in the given linked list.
    # Auxiliary Space: O(n)
    # ================================================================================================================
    # Another Approach: Create a pointer that will point towards the first occurrence of every element and
    # another pointer temp which will iterate to every element and when the value of the previous pointer is not equal to the temp pointer,
    # we will set the pointer of the previous pointer to the first occurrence of another node.
    def removeDuplicatesPointerMethod (self):
        if self.head is None and self.head is None:
            return
        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return

    # Time Complexity: O(n) where n is the number of nodes in the given linked list.
    # Auxiliary Space: O(1) 

if __name__ == '__main__':
    ll = LinkedList ()
    ll.insertion (10)
    ll.insertion (10)
    ll.insertion (11)
    ll.insertion (11)
    ll.insertion (31)
    ll.insertion (31)
    ll.insertion (33)
    ll.traversal ()
    # ll.removeDuplicates ()
    # ll.removeDupilicatesRecursiveWrapper ()
    ll.removeDuplicatesPointerMethod ()
    ll.traversal ()