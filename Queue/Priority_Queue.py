# PRIORITY QUEUE
# Each element has a priority (higher priority = gets removed first)
# Can be implemented using a list, PriorityQueue, or custom class

############################################################################

# LIST
# Pros: Easy to implement, easy indexing because of contiguous memory
# Cons: Takes longer since you have to sort the list

print('')
print('')

print('***** LIST IMPLEMENTATION *****')

# Creation
pqList = []

# Enqueue
pqList.append((4,'Fourth'))
pqList.append((1,'First'))
pqList.append((3,'Third'))
pqList.append((2,'Second'))

# Sort queue
pqList.sort()
# Output: [(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')]
print(pqList)

# Dequeue
pqList.pop()
pqList.pop()
pqList.pop()
print("Expected Output: [(1, 'First')]")
print("Actual Output: " + str(pqList))

print('')
print('')

############################################################################

# PriorityQueue
# Pros: Easy to implement
# Cons: Always dequeues in ascending order (no way to modify the ordering)

print('***** PRIORITYQUEUE IMPLEMENTATION *****')

# import PriorityQueue from queue
from queue import PriorityQueue

# Creation
pqMod = PriorityQueue()

# Enqueue
pqMod.put((3,'Third'))
pqMod.put((1,'First'))
pqMod.put((2,'Second'))

# Dequeue
print('Deque Test')
print("Expected Output: [(1, 'First')]")
print("Actual Output: " + str(pqMod.get()))

print("Expected Output: [(2, 'Second')]")
print("Actual Output: " + str(pqMod.get()))

print('')
print('')


############################################################################

# CUSTOM CLASS
# Pros: See what each method does
# Cons: Harder to implement

print('***** CUSTOMCLASS IMPLEMENTATION *****')

class PQ():
    def __init__(self):
        self.queue = []

    # Enqueue
    # Adds element to the back
    # Time Complexity: O(1)
    def enqueue(self,data):
        self.queue.append(data)
        print(str(data) + ' has been enqueued.')

    # Dequeue
    # Removes element from the front
    # Time Complexity: O(n)
    def dequeue(self):

        # Store priorities
        temp = 0

        # Find index in which the priority is greatest
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[temp]:
                temp = i
        item = self.queue[temp]
        self.queue.pop(temp)
        print(str(item) + ' has been dequeued.')

# TESTS

pqCC = PQ()

# Enqueue Test
print('Enqueue Test')
print("Expected Order of Output: 3,2,5,1")
pqCC.enqueue(3)
pqCC.enqueue(2)
pqCC.enqueue(5)
pqCC.enqueue(1)

# Dequeue Test
print('Dequeue Test')
print("Expected Order of Output: 5,3,2")
pqCC.dequeue()
pqCC.dequeue()
pqCC.dequeue()
