# CIRCULAR QUEUE 
# Last element points to the first item, creating a "circular" link

# Create Circular Queue Class
class CircularQueue():

    # Set front and rear to the same position, set a maxsize
    def __init__(self,maxSize):
        self.front=0
        self.rear=0
        self.maxSize = maxSize
        self.queue = []

    # Enqueue
    # Adds element to the back
    # Time Complexity: O(1)
    def enqueue(self, data):
        # If queue is full
        if self.size() == self.maxSize -1:
            print('Queue is full.')
        
        else:
            # Append data and increment rear pointer
            self.queue.append(data)
            
            # Increment rear
            # self.rear+=1 - This would make sense if it wasn't circular but we need to wrap around to the start of the queue once it exceeds maxSize
            self.rear = (self.rear+1) % self.maxSize

            print(str(data) + ' has been enqueued.')

    # Dequeue
    # Removes element from the front
    # Time Complexity: O(1)
    def dequeue(self):
        # If queue is empty
        if self.size() == 0:
            print('Queue is empty.')
        
        else:
            # Get data of front
            data = self.queue[self.front]

            # increment front pointer
            # self.front+=1 - This would make sense if it wasn't circular but we need to wrap around to the start of the queue once it exceeds maxSize
            self.front = (self.front+1) % self.maxSize

            print(str(data) + ' has been dequeued.')
    
    # Size
    # Get size of queue
    # Time Complexity: O(n)
    def size(self):
        # If rear greater or equal to front, size is rear - front
        if self.rear >= self.front:
            return self.rear - self.front
        # If front is greater than rear
        return self.maxSize - (self.front - self.rear)


# TESTS

size = input('Enter the size of the circular queue: ')
queue = CircularQueue(int(size))

# Assuming Size is 5:
# Enqueue
print('Enqueue Test: Add 1-4')
# Expected Order of Enqueue: 1,2,3,4
# Actual Order of Enqueue: 1,2,3,4
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print('Expected Output: Queue is full.')
queue.enqueue(5)

# Size
print('Size Test')
# Expected Output: 5
# Actual Output: 5
print('Expected Output: 4')
print('Actual Output: ' + str(queue.size()))

# Dequeue
print('Dequeue Test')
# Expected Order of Enqueue: 1,2,3,4,5 
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print('Expected Output: Queue is empty.')
queue.dequeue()





        
