# Union and Intersection of two Linked List using Hashing
# Input:
#    List1: 10 -> 15 -> 4 -> 20
#    List2: 8 -> 4 -> 2 -> 10
# Output:
#    Intersection List: 4 -> 10
#    Union List: 2 -> 8 -> 20 -> 4 -> 15 -> 10
# Explanation: In this two lists 4 and 10 nodes 
# are common. The union lists contains 
# all the nodes of both the lists.

# Input:
#    List1: 1 -> 2 -> 3 -> 4
#    List2: 3 -> 4 -> 8 -> 10
# Output:
#    Intersection List: 3 -> 4
#    Union List: 1 -> 2 -> 3 -> 4 -> 8 -> 10
# Explanation: In this two lists 4 and 3 nodes 
# are common. The union lists contains 
# all the nodes of both the lists.

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

# Implementation:
# 1- Start traversing both the lists.
#    a) Store the current element of both lists
#       with its occurrence in the map.
# 2- For Union: Store all the elements of the map 
#    in the resultant list.
# 3- For Intersection: Store all the elements only 
#    with an occurrence of 2 as 2 denotes that 
#    they are present in both the lists.

def traversal (head):
    while head:
        print (head.data, end = ' -> ')
        head = head.next
        if head is None:
            print ('None')

def intersectionUsingHashing (firstLL, secondLL):
    hashmap = {}
    while firstLL is not None:
        data = firstLL.data
        if data not in hashmap.keys():
            hashmap[data] = 1
        firstLL = firstLL.next

    result = LinkedList ()
    while secondLL is not None:
        data = secondLL.data
        if data in hashmap.keys ():
            result.insert (data)
        secondLL = secondLL.next
    return result.head

def unionUsingHashing (firstLL, secondLL):
    hashmap = {}
    while firstLL is not None:
        data = firstLL.data
        if data not in hashmap.keys ():
            hashmap[data] = 1
        firstLL = firstLL.next

    while secondLL is not None:
        data = secondLL.data
        if data not in hashmap.keys ():
            hashmap[data] = 1
        secondLL = secondLL.next

    result = LinkedList ()
    for key, value in hashmap.items ():
        result.insert (key)
    return result.head

# Time Complexity: O(m+n). Here ‘m’ and ‘n’ are number of elements present in first and second lists respectively.
#     Reason: For Union: Traverse both the lists, store the elements in Hash-map and update the respective count.
#     For Intersection: Check if count of an element in hash-map is ‘2’.
# Auxiliary Space: O(m+n). Use of Hash-map data structure for storing values.

if __name__ == '__main__':
    first = LinkedList ()
    first.insert (1)
    first.insert (2)
    first.insert (3)
    print ('First Linked List')
    traversal (first.head)

    second = LinkedList ()
    second.insert (1)
    second.insert (9)
    print ('Second Linked List')
    traversal (second.head)

    print ('Intersection Elements of 2 Lists')
    traversal (intersectionUsingHashing (first.head, second.head))

    print ('Union Elements of 2 Lists')
    traversal (unionUsingHashing (first.head, second.head))


