# DEQUE
# Double-ended queue, where insertion and deletion can be performed in the front or rear
# Pretty similar to Queue implementation except you can insert at front and delete at rear

# Create Deque Class
class Deque():
    def __init__(self):
        self.items = []
    
    # Check if the array is empty
    # Time Complexity: O(1)
    def isEmpty(self):
        # Will return true or false
        return self.items == []

    # Get the size of the array
    # Time Complexity: O(1)
    def size(self):
        return len(self.items)

    # Add element to front
    # We would use the insert method to specify insertion at the beginning
    # Time Complexity: O(1)
    def addFront(self, data):
        self.items.insert(0, data)
        print(str(data) + " has been added at the front.")

    # Add element to the rear
    # We would use the append method
    # Time Complexity: O(1)
    def addRear(self,data):
        self.items.append(data)
        print(str(data) + " has been added at the rear.")

    # Delete element at the front
    # We would use the pop method with a parameter of 0
    # Time Complexity: O(1)
    def deleteFront(self):
        print( str(self.items.pop(0)) + " has been deleted.")

    # Delete element at the rear
    # We would use the pop method with 0 parameter (removes the rear by default)
    # Time Complexity: O(1)
    def deleteRear(self):
        print( str(self.items.pop()) + " has been deleted.")


# TEST

# Initialize Deque
deque = Deque()

# Insert at Front
deque.addFront(2)
deque.addFront(1)

# Insert at Rear
deque.addRear(3)
deque.addRear(4)

print("Expected Output: 1234")

# Delete at Front
print("Expected Value of Deletion: 1")
deque.deleteFront()
print("Expected Value of Deletion: 2")
deque.deleteFront()

# Delete at Rear
print("Expected Value of Deletion: 4")
deque.deleteRear()