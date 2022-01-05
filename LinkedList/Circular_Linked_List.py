# CIRCULAR (DOUBLY) LINKED LIST
# Nodes are connected to form a "circle" (ending node points to starting node, not NULL)
# Can be implemented using singly or doubly


class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    # GETTER AND SETTER METHODS

    # Get data
    def get_data(self):
        return self.data

    # Get next node
    def get_next(self):
        return self.next

    # Get prev node
    def get_prev(self):
        return self.prev

    # Set next node
    def set_next(self, new_next):
        self.next = new_next

    # Set prev node
    def set_prev(self, new_prev):
        self.prev = new_prev


class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    # OPERATIONS

    # Insert Front 
    # Initializes a new node with the data and adds it to the front of the list
    # Time Complexity: O(1)
    def insertFront(self,data):
        # Create new node with the data
        new_node = Node(data)

        # If the list is empty, set new_node to head, next and prev to null
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.tail

        # If list isn't empty
        else:
            # Set next node of tail to new node
            self.head.set_prev(new_node)
            # Set previous of new node to tail
            new_node.set_next(self.head)
            # Set tail to new node
            self.head = new_node
            # Set next node of tail to head
            self.head.set_prev(self.tail)
            self.tail.set_next(self.head)


    # Insert at Specified Position
    # Initializes a new node with the data and adds it at the specified position
    # Time Complexity: O(n)
    # note: position is not 0-index based
    def insertAt(self,data,position):
        # Create new node with the data
        new_node = Node(data)

        # Check for position > 1
        if position < 1:
            print('Please input a position greater than or equal to 1.')
        
        elif position > self.size():
            print('Position is out of bounds.')

        # If position is 1, set new node to head
        elif position == 1:
            # Set next node of tail to new node
            self.head.set_prev(new_node)
            # Set previous of new node to tail
            new_node.set_next(self.head)
            # Set tail to new node
            self.head = new_node
            # Set next node of tail to head
            self.head.set_prev(self.tail)
            self.tail.set_next(self.head)
            print('Node with ' + str(data) + ' has been added at position ' + str(position) + '.')

        # If position is last
        elif position == self.size() + 1:
            # Set next node of tail to new node
            self.tail.set_next(new_node)
            # Set previous of new node to tail
            new_node.set_prev(self.tail)
            # Set tail to new node
            self.tail = new_node
            # Set next node of tail to head
            self.tail.set_next(self.head)
            self.head.set_prev(self.tail)
            print('Node with ' + str(data) + ' has been added at position ' + str(position) + '.')

        else:
            # Create temp node, traverse to node before position
            temp = self.head.get_next()
            for x in range(1, position-2):
                temp = temp.get_next()
            new_node.set_next(temp.get_next())
            new_node.set_prev(temp)
            temp.set_next(new_node)
            print('Node with ' + str(data) + ' has been added at position ' + str(position) + '.')

    # Insert BackMyLinkedList.printListForward()
    # Initializes a new node with the data and adds it to the end of the list
    # Time Complexity: O(n)
    def insertBack(self,data):
        # Create new node with the data
        new_node = Node(data)

        # If the list is empty, set new_node to head, next and prev to null
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head

        # If list isn't empty
        else:
            # Set next node of tail to new node
            self.tail.set_next(new_node)
            # Set previous of new node to tail
            new_node.set_prev(self.tail)
            # Set tail to new node
            self.tail = new_node
            # Set next node of tail to head
            self.tail.set_next(self.head)
            self.head.set_prev(self.tail)

    
    # Size
    # Returns size of the linked list
    # Time Complexity: O(n)
    def size(self):
        curr = self.head.get_next()
        count = 0
        while curr != self.head:
            count += 1
            curr = curr.get_next()
        return count + 1

    
    # Search
    # Looks for data in the list
    # Returns true if found, false otherwise
    # Time Complexity: O(n)
    def search(self,data):

        # If list is empty
        if self.head == None:
            print('The list is empty.')
            return False
            
        curr = self.head.get_next()
        while curr != self.head:
            if curr.get_data() == data:
                print('The node containing ' + str(data) + ' has been found.')
                return True
            else:
                curr = curr.get_next()
        print('The node containing ' + str(data) + ' has not been found.')
        return False


    # Delete
    # Removes Node with the data
    # Returns true if successful, false if unsuccessful
    # Time Complexity: O(n)
    def delete(self,data):

        # If list is empty
        if self.head == 0:
            print('The list is empty.')
            return False

        curr = self.head.get_next()
        #prev = self.prev
        while curr != self.head:
            # If node found, delete by changing next node ref of prev to next node of curr
            if curr.get_data() == data:
                curr.get_prev().set_next(curr.get_next())
                curr.set_next(None)
                curr.set_prev(None)
                print('The node containing ' + str(data) + ' has been deleted.')
                return True
            else:
                curr.prev = curr
                curr = curr.get_next()
        print('There is no node containing ' + str(data) + '.')
        return False


    # Print List Forward
    # Prints the linked list going forwards
    # Time Complexity: O(n)
    def printListForward(self):
        temp = self.head
        if temp != None:
            print('The list in forwards order is ', end=" ")
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break
            print()
        else:
            print('This list is empty.')
    
    # Print List Backward
    # Prints the linked list going backwards
    # Time Complexity: O(n)
    def printListBackward(self):
        temp = self.tail
        if temp != None:
            print('The list in backwards order is ', end=" ")
            while True:
                print(temp.data, end=" ")
                temp = temp.prev
                if (temp == self.tail):
                    break
            print()
        else:
            print('This list is empty.')



# TESTS

# Create new Linked List
MyLinkedList = CircularLinkedList()

# Insert Back Test
print('Insert Back Test')
MyLinkedList.insertBack(4)
MyLinkedList.insertBack(5)
MyLinkedList.insertBack(6)
print('Expected Output: 4,5,6')
MyLinkedList.printListForward()

# Insert Front Test
print('Insert Front Test')
MyLinkedList.insertFront(3)
MyLinkedList.insertFront(2)
MyLinkedList.insertFront(1)
print('Expected Output: 1,2,3,4,5,6')
MyLinkedList.printListForward()

print('Print List Backward Test')
print('Expected Output: 6,5,4,3,2,1')
MyLinkedList.printListBackward()

# Insert At Test
print('Insert At Test: Insert 0 at position 1')
print('Expected Output: 0,1,2,3,4,5,6')
MyLinkedList.insertAt(0,1)
MyLinkedList.printListForward()
print('Size after insertion: ' + str(MyLinkedList.size()))

print('Insert At Test: Insert 7 at position 7')
print('Expected Output: 0,1,2,3,4,5,7,6')
MyLinkedList.insertAt(7,7)
MyLinkedList.printListForward()

print('Expected Output: 0,1,2,8,3,4,5,7,6')
MyLinkedList.insertAt(8,4)
MyLinkedList.printListForward()
print('Size after insertion: ' + str(MyLinkedList.size()))

# Search Test
print('Search Test: 7')
print('Expected Output: The node containining 7 has been found.')
MyLinkedList.search(7)

print('Search Test: 10')
print('Expected Output: The node containining 10 has not been found.')
MyLinkedList.search(10)

# Delete Test
print('Delete Test: 4')
print('Expected Output: The node containing 4 has been deleted.')
MyLinkedList.delete(4)

print('Expected Output: 0,1,2,8,3,5,7,6')
MyLinkedList.printListForward()

print('Delete Test: 10')
print('Expected Output: There is no node containing 10.')
MyLinkedList.delete(10)

print('Expected Output: 0,1,2,8,3,5,7,6')
MyLinkedList.printListForward()




    

    

    




