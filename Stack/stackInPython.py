# Implementation using list
class StackUsingArray:
    stack = list()
    def __init__(self):
        self.stack.append('a')
        self.stack.append('b')
        self.stack.append('c')
        print (f'Initial Stack {self.stack}')
        self.stack.pop()
        self.stack.pop()
        print (f'Stack after popping elements {self.stack}')


# Implementation using collections.deque:
# Python stack can be implemented using the deque class from the collections module.
# Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container,
# as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 

from collections import deque

class StackUsingDeque:
    def __init__ (self):
        stack = deque ()
        stack.append('a')
        stack.append('b')
        stack.append('c')        
        print(f'Initial stack {stack}')
        stack.pop()
        stack.pop()
        print(f'Stack after elements are popped {stack}')


# Implementation using queue module :
# Queue module also has a LIFO Queue, which is basically a Stack.
# Data is inserted into Queue using the put() function and get() takes data out from the Queue. 

from queue import LifoQueue

class StackUsingQueue:
    def __init__ (self):
        stack = LifoQueue(maxsize=3)
        print(stack.qsize())

        stack.put('a')
        stack.put('b')
        stack.put('c')
        
        print("Full: ", stack.full())
        print("Size: ", stack.qsize())
        
        print('\nElements popped from the stack')
        print(stack.get())
        print(stack.get())
        
        print("\nEmpty: ", stack.empty())

# Implementation using a singly linked list 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
 
    def getSize(self):
        return self.size
 
    def isEmpty(self):
        return self.size == 0
 
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
    

if __name__ == '__main__':
    stack = StackUsingLinkedList()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
 
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")

