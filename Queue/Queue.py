# QUEUE
# First in, first out (element that gets inserted first will be removed first)
# 2 main operations: enqueue (add element to the back), dequeue (remove element from front). Both operations take O(1) time.
# Can be implemented using list, deque, or Queue

############################################################################

# LIST
# Pros: Easy to implement, easy indexing because of contiguous memory
# Cons: Takes longer to add to the list, threading problems

print('')
print('')

print('***** LIST IMPLEMENTATION *****')

# Create Queue Class
class Queue:
    def __init__(self):
        self.elements = []
    
    # OPERATIONS

    # Enqueue
    # Adds element to the back
    # Time Complexity: O(1)
    def enqueue(self, data):
        self.elements.append(data)
        print(str(data) + ' has been enqueued.')

    # Dequeue
    # Removes element from the front
    # Time Complexity: O(1)
    def dequeue(self):
        print(str(self.elements[0]) + ' has been dequeued.')
        self.elements.pop(0)
        

# TESTS

queue = Queue()

# Enqueue Test
print('Enqueue Test')
print('Expected Order of Output: 1,2,3')
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue Test
print('Dequeue Test')
print('Expected Order of Output: 1,2,3')
queue.dequeue()
queue.dequeue()
queue.dequeue()

print(' ')
print(' ')

############################################################################

print('***** DEQUE IMPLEMENTATION *****')

# DEQUE (double-ended queue, doubly linked list)
# Pros: Can add nodes easily to any end of the list
# Cons: Problems arise if you're threading

# Import deque from collections
from collections import deque

# CREATION
queueDeque = deque()

# Enqueue
print('Enqueue Test')
queueDeque.append(1)
queueDeque.append(2)
queueDeque.append(3)

print('Expected Output: [1,2,3]')
print(queueDeque)

# Dequeue
print('Dequeue Test')
queueDeque.popleft()
queueDeque.popleft()

print('Expected Output: [3]')
print(queueDeque)

print(' ')
print(' ')

############################################################################

print('***** QUEUE IMPLEMENTATION *****')

# Queue (Similar to list implementation)
# Pros: See List
# Cons: See List

# import Queue from queue
from queue import Queue

# CREATION
queueQueue = Queue()

# OPERATIONS

# Enqueue
print('Enqueue Test')
queueQueue.put(1)
print('1 has been enqueued.')
queueQueue.put(2)
print('2 has been enqueued.')
queueQueue.put(3)
print('3 has been enqueued.')


# Dequeue
print('Dequeue Test')
print(str(queueQueue.get()) + ' has been dequeued.')
print(str(queueQueue.get()) + ' has been dequeued.')








    




