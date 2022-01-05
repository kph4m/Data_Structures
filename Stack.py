# STACK
# Abstract Data Type
# Last in, first out (element that is added last will be removed first)
# 2 main operations: push (add to stack), pop (remove top value from stack and returns it). Both of which run in O(1) time.
# Can be implemented using list, deque, LifoQueue, or singly linked list

############################################################################

# LIST
# Pros: Easy to implement, easy indexing because of contiguous memory
# Cons: Takes longer to add to the list, threading problems

print('')
print('')

print('***** LIST IMPLEMENTATION *****')

# CREATION
stackList = []

# OPERATIONS

# Push
stackList.append(1)
stackList.append(2)
stackList.append(3)
print('Push Test: push 1,2,3')
print('Expected Output: [1,2,3]')
print('Actual Output: ' + str(stackList))

# Pop
# Output: 3
stackList.pop()
print('Pop Test: pop top element')
print('Expected Output: [1,2]')
print('Actual Output: ' + str(stackList))

print('')
print('')
############################################################################

# DEQUE (double-ended queue, doubly linked list)
# Pros: Can add nodes easily to any end of the list
# Cons: Problems arise if you're threading

print('***** DEQUE IMPLEMENTATION *****')

# import deque from collections
from collections import deque

# CREATION
stackDeque = deque()

# OPERATIONS

# Push
stackDeque.append(1)
stackDeque.append(2)
stackDeque.append(3)
print('Push Test: push 1,2,3')
print('Expected Output: [1,2,3]')
print('Actual Output: ' + str(stackDeque))

# Pop
# Output: 3
stackDeque.pop()
print('Pop Test: pop top element')
print('Expected Output: [1,2]')
print('Actual Output: ' + str(stackDeque))

print('')
print('')

############################################################################

# LifoQueue
# Pros: Good if you're threading
# Cons: Takes longer for operations

print('***** LIFOQUEUE IMPLEMENTATION *****')

# import LifoQueue from queue
from queue import LifoQueue

# CREATION
stackLifo = LifoQueue()

# OPERATIONS

# Push
stackLifo.put(1)
stackLifo.put(2)
stackLifo.put(3)

# Pop
# Output Order of Removal: 3,2,1
for i in range(1,4):
    print(str(stackLifo.get())  + " has been removed from the top of the stack.")

print('')
print('')

############################################################################

# SINGLY LINKED LIST
# Pros: Understand what the methods do
# Cons: Harder to implement, can't traverse both directions like deque

print('***** SINGLY LINKED LIST IMPLEMENTATION *****')

class Node:

    def __init__(self, data):
      self.data = data
      self.next = None

    # GETTER AND SETTER METHODS

    # Get data
    def get_data(self):
        return self.data

    # Set next
    def set_next(self, new_next):
        self.next = new_next


 
class Stack:
    def __init__(self, head=None):
       # Use dummy head node
      self.head = Node(head)
      self.size = 0
 
   # OPERATIONS

    # isEmpty
    # Check if stack is empty
    # Time Complexity: O(1)
    def isEmpty(self):
        return self.size == 0

    # Peek
    # Return the element at the top of the stack
    # Time Complexity: O(1)# Pros: Easy to implement, easy indexing because of contiguous memory
# Cons: Takes longer to add to the list, threading problems
    def peek(self):
        # Check for empty stack
        if self.size == 0:
            raise Exception('Stack is empty.')

        else:
            # Get data of node to return it
            top_node = self.head.next.get_data()
            return top_node

    # Pop
    # Remove and return the top value
    # Time Complexity: O(1)
    def pop(self):
        # Check for empty stack
        if self.size == 0:
            raise Exception('Stack is empty.')

        else:
            # Node we're going to remove
            remove = self.head.next

            # Set next node of head to next next node of head
            self.head.set_next(self.head.next.next)

            # Decrement size
            self.size -= 1

            print(str(remove.data) + ' has been popped from the stack.')

            return remove.data

    # Push
    # Add node to the top of the stack
    # Time Complexity: O(1)
    def push(self, data):

        # Create new node with data
        new_node = Node(data)

        # Set next of node to previous head next
        new_node.set_next(self.head.next)

        # Set head next to the node
        self.head.set_next(new_node)

        # Increment Size
        self.size += 1

        print(str(data) + ' has been pushed to the stack.')

 
# TESTS

stack = Stack()

# PUSH TEST
# Expected Output Order of Addition: 5,6,7,8,9
# Actual Output Order of Addition: 5,6,7,8,9
print('Push Test: elements 5-9')
for i in range(5,10):
    stack.push(i)

# PEEK TEST
print('Peek Test: get top element')
print("Expected Output: 9")
print("Actual Output: " + str(stack.peek()))

# ISEMPTY TEST
print('Isempty Test: Check if list is empty')
print("Expected Output: False ")
print("Actual Output:  " + str(stack.isEmpty()))

# POP TEST
print('Pop Test: remove top 5 elements')
# Expected Output Order of Removal: 9,8,7,6,5
# Actual Output Order of Removal: 9,8,7,6,5
for i in range(5):
    remove = stack.pop()
    




