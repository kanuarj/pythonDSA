# Intersection of two Sorted Linked Lists

# Given two lists sorted in increasing order, create and return a new list representing the intersection of the two lists.
# The new list should be made with its own memory — the original lists should not be changed. 

# Example: 
# Input: 
# First linked list: 1->2->3->4->6
# Second linked list be 2->4->6->8, 
# Output: 2->4->6.
# The elements 2, 4, 6 are common in 
# both the list so they appear in the 
# intersection list. 

# Input: 
# First linked list: 1->2->3->4->5
# Second linked list be 2->3->4, 
# Output: 2->3->4
# The elements 2, 3, 4 are common in 
# both the list so they appear in the 
# intersection list.

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def insertion (head, newData):
    newNode = Node (newData)
    newNode.next = head
    head = newNode
    return newNode

def traversal (temp):
    while temp:
        print (temp.data, end = ' -> ')
        temp = temp.next
        if temp is None:
            print ('None')

# Method : Using Local References. 
def localReferencesMethod (firstLL, secondLL):
    result = Node (0)
    current = result
    while firstLL is not None and secondLL is not None:
        if firstLL.data == secondLL.data:
            current.next = Node (firstLL.data)
            current = current.next
            firstLL = firstLL.next
            secondLL = secondLL.next
        elif firstLL.data < secondLL.data:
            firstLL = firstLL.next
        else:
            secondLL = secondLL.next
    result = result.next
    return result

# Complexity Analysis: 
# Time Complexity: O(m+n) where m and n are number of nodes in first and second linked lists respectively. 
# Only one traversal of the lists are needed.
# Auxiliary Space: O(max(m, n)). 
# The output list can store at most m+n nodes.
# ===============================================================================================================
# Method : Recursive Solution
def recursiveSolution (firstLL, secondLL):
    if (firstLL is None or secondLL is None):
        return None

    if (firstLL.data < secondLL.data):
        return recursiveSolution (firstLL.next, secondLL)

    if (firstLL.data > secondLL.data):
        return recursiveSolution (firstLL, secondLL.next)

    temp = Node (0)
    temp.data = firstLL.data
    temp.next = recursiveSolution (firstLL.next, secondLL.next)
    return temp

# Complexity Analysis: 
# Time Complexity: O(m+n) where m and n are number of nodes in first and second linked lists respectively. 
# Only one traversal of the lists are needed.
# Auxiliary Space: O(max(m, n)). 
# The output list can store at most m+n nodes.

if __name__ == '__main__':
    firstLL = secondLL = intersectionList = None

    firstLL = insertion (firstLL, 5)
    firstLL = insertion (firstLL, 4)
    firstLL = insertion (firstLL, 3)
    traversal (firstLL)

    secondLL = insertion (secondLL, 7)
    secondLL = insertion (secondLL, 6)
    secondLL = insertion (secondLL, 5)
    traversal (secondLL)

    # intersectionList = localReferencesMethod (firstLL, secondLL)
    # traversal (intersectionList)

    intersectionList = recursiveSolution (firstLL, secondLL)
    traversal (intersectionList)


