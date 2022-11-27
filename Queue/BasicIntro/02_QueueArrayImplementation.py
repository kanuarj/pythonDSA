# Time Complexity
# Enqueue(insertion) - O(1)
# Deque(deletion) - O(1)
# Front(Get front) - O(1)
# Rear(Get Rear) - O(1)
                           
# Auxiliary Space: 
# O(N) where N is the size of the array for storing elements.

class Queue:
    def __init__ (self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # The capacity of the Queue is Full when the size is equal to its capacity
    def isFull (self):
        return self.size == self.capacity

    # The size of the Queue is equal to zero defines it is empty 
    def isEmpty (self):
        return self.size == 0

    # The operation to add an item to queue from rear
    def enqueueOperation (self, item):
        if self.isFull():
            print ('Queue is Full')
            return
        
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print (f'The {str(item)} has been enqueued into the queue')

    # The operation to delete an item from the queue from front 
    def dequeOperation (self):
        if self.isEmpty():
            print ('Queue is Empty')
            return

        print (f'The {str(self.Q[self.front])} has been dequeued from the queue')
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    # Retrieve the front element of the queue 
    def frontElement (self):
        if self.isEmpty ():
            print ('The queue is empty')

        print (f'The element in the front of the queue is {self.Q[self.front]}')

    # Retrieve the rear element of the queue 
    def rearElement (self):
        if self.isFull ():
            print ('The queue is full')

        print (f'The element in the rear of the queue is {self.Q[self.rear]}')


if __name__ == '__main__':
    queue = Queue (30)
    queue.enqueueOperation (10)
    queue.enqueueOperation (20)
    queue.enqueueOperation (30)
    queue.enqueueOperation (40)
    queue.dequeOperation ()
    queue.frontElement ()
    queue.rearElement ()