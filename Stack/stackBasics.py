# Implementation of Stack using Arrays

# Advantages of array implementation:
# - Easy to implement.
# - Memory is saved as pointers are not involved.

# Disadvantages of array implementation:
# - It is not dynamic i.e., it doesn’t grow and shrink depending on needs at runtime. 
#   [But in case of dynamic sized arrays like vector in C++, list in Python, ArrayList in Java, 
#       stacks can grow and shrink with array implementation as well].
# - The total size of the stack must be defined beforehand.

from sys import maxsize

class StackUsingArrays:
    def createStack (self):
        stack = list()
        return stack

    def isEmpty (self, stack):
        return len(stack) == 0

    def push (self, stack, item):
        stack.append (item)
        print (f"The {item} has been pushed to stack")

    def pop (self, stack):
        if (self.isEmpty(stack)):
            return str (-maxsize - 1)
        stack.pop()

    def peek (self, stack):
        if (self.isEmpty (stack)):
            return str (-maxsize - 1)
        return stack[len(stack)-1]

# Implementation of Stack using Linked List 

# Advantages of Linked List implementation:
# The linked list implementation of a stack can grow and shrink according to the needs at runtime.
# It is used in many virtual machines like JVM.

# Disadvantages of Linked List implementation:
# Requires extra memory due to the involvement of pointers.
# Random accessing is not possible in stack.

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__ (self):
        self.root = None

    def isEmpty (self):
        return True if self.root is None else False

    def push (self, newData):
        newNode = Node (newData)
        newNode.next = self.root
        self.root = newNode
        print (f'The element {newData} has been pushed onto Stack')

    def pop (self):
        if (self.isEmpty ()):
            return float ('-inf')
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek (self):
        if self.isEmpty ():
            return float ('-inf')
        return self.root.data


if __name__ == '__main__':
    # stack = StackUsingArrays ()
    # s = stack.createStack ()
    # stack.push (s, str(10))
    # stack.push (s, str(20))
    # val = stack.peek (s)
    # print (val)
    # stack.pop (s)
    # val = stack.peek (s)
    # print (val)
    # print (stack.isEmpty (s))

    stack = Stack ()
    stack.push (10)
    stack.push (20)
    stack.push (30)
    print (f'The element {stack.pop()} is popped')
    print (f'The top element in the stack is {stack.peek()}')
