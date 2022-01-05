# SINGLY LINKED LIST IN PYTHON

# Linked List is a data structure in which each element/node is a separate object.
# Each node contains 2 main pieces of info: Data, Reference to node(s)
# First node is called the Head node
# Last node is called the Tail node

# Singly: each node has reference to next node

# Create Node Class
class Node():
    # Initialize data and next node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # GETTER AND SETTER METHODS

    # Get data
    def get_data(self):
        return self.data

    # Get next node
    def get_next(self):
        return self.next

    # Set next node
    def set_next(self, new_next):
        self.next = new_next

# Create Linked List class
class LinkedList():
    def __init__(self, head=None):
        self.head = head

    # OPERATIONS

    # Insert Front 
    # Initializes a new node with the data and adds it to the front of the list
    # Time Complexity: O(1)
    def insertFront(self,data):
        # Create new node with the data
        new_node = Node(data)

        # If the list is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        # If list isn't empty
        else:
            new_node.set_next(self.head)
            self.head = new_node

    
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

        # If position is 1, set new node to head
        elif position == 1:
            new_node.set_next(self.head)
            self.head = new_node
            print('Node with ' + str(data) + ' has been added at position ' + str(position) + '.')


        else:
            # Create temp node, traverse to node before position
            temp = self.head
            for x in range(1, position-1):
                if temp != None:
                    temp = temp.get_next()
            
            # If no value at temp, traversed out of bounds
            if temp == None:
                print('Reached a null node, not possible to insert at this position')
            else:
                # Set appropriate relations
                new_node.set_next(temp.get_next())
                temp.set_next(new_node)
                print('Node with ' + str(data) + ' has been added at position ' + str(position) + '.')


    # Insert Back
    # Initializes a new node with the data and adds it to the end of the list
    # Time Complexity: O(n)
    def insertBack(self,data):

        # Create new node with the data
        new_node = Node(data)

        # If the list is empty
        if (self.head == None):
            self.head = new_node
        # If list isn't empty
        else:
            # Create temp node and set to head
            temp = self.head
            # Keep traversing until temp node next is empty
            while temp.get_next() != None:
                temp = temp.get_next()
            # Set the temp node next to the new node
            temp.set_next(new_node)


    # Search
    # Looks for data in the list
    # Returns true if found, false otherwise
    # Time Complexity: O(n)
    def search(self,data):

        # If list is empty
        if self.head == None:
            print('The list is empty.')
            return False
            

        curr = self.head
        while curr:
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

        curr = self.head
        prev = None
        while curr:
            # If node found, delete by changing next node ref of prev to next node of curr
            if curr.get_data() == data:
                prev.set_next(curr.get_next())
                print('The node containing ' + str(data) + ' has been deleted.')
                return True
            else:
                prev = curr
                curr = curr.get_next()
        print('There is no node containing ' + str(data) + '.')
        return False


    # Size
    # Returns size of the linked list
    # Time Complexity: O(n)
    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        print('The size of the list is' + ' ' + str(count) + '.')
        return count


    # Print List
    # Prints the linked list
    # Time Complexity: O(n)
    def printList(self):

        # If list is empty
        if (self.head == None):
            print('The list is empty.')
        
        # If list isn't empty
        else:
            temp = self.head
            print('The list contains', end=" ")
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.get_next()
            print()


# TESTS

# Create new Linked List
MyLinkedList = LinkedList()

# Insert Front Test
print('Insert Front Test')
MyLinkedList.insertFront(3)
MyLinkedList.insertFront(2)
MyLinkedList.insertFront(1)
print('Expected Output: 1,2,3')
MyLinkedList.printList()

# Insert Back Test
print('Insert Back Test')
MyLinkedList.insertBack(4)
MyLinkedList.insertBack(5)
MyLinkedList.insertBack(6)
print('Expected Output: 1,2,3,4,5,6')
MyLinkedList.printList()

# Size Test
print('Expected Output: 6')
MyLinkedList.size()

# Search Test
print('Search Test')
print('Expected Output: The node containing 3 has been found.')
MyLinkedList.search(3)

print('Expected Output: The node containing 7 has been found.')
MyLinkedList.search(7)

# Delete Test
print('Delete Test')
print('Expected Output: The node containing 6 has been deleted.')
MyLinkedList.delete(6)

print('Expected Output: 1,2,3,4,5')
MyLinkedList.printList()

print('Expected Output: There is no node containing 8.')
MyLinkedList.delete(8)

print('Expected Output: 1,2,3,4,5')
MyLinkedList.printList()


# Insert At Test
print('Insert At Test')
print('Expected Output: Node with 6 has been added at position 3.')
MyLinkedList.insertAt(6,3)

print("Expected Output: 1,2,6,3,4,5")
MyLinkedList.printList()

print('Expected Output: Node with 7 has been added at position 1.')
MyLinkedList.insertAt(7,1)

print('Expected Output: 7,1,2,6,3,4,5')
MyLinkedList.printList()

print('Expected Output: Node with 8 has been added at position 8.')
MyLinkedList.insertAt(8,8)

print('Expected Output: 7,1,2,6,3,4,5,8')
MyLinkedList.printList()

print('Expected Output: Please input a position greater than or equal to 1.')
MyLinkedList.insertAt(9,0)




