# BINARY SEARCH TREE
# Good for maintaining a sorted list of numbers
# Search time complexity can be done in logarithmic time: O(log(n))
# All nodes in left subtree are less than the root node
# All nodes in right subtree are greater than the root node

# NODE CLASS
class BSTNode:
    def __init__(self,data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Min
    # Get min value of the tree, which is the left-most node
    # Time Complexity: O(n)
    def min(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.data

    # Max
    # Get max value of the tree, which is the right-most node
    # Time Complexity: O(n)
    def max(self):
        curr = self
        while curr.right is not None:
            curr = curr.right
        return curr.data
    
    # Inorder
    # Traverse left subtree -> root -> right subtree
    # Time Complexity: O(n)
    def inorder(self,datas):
        # If left child isn't null, traverse left subtree
        if self.left is not None:
            self.left.inorder(datas)
        # If root not null, add to data list
        if self.data is not None:
            datas.append(self.data)
        # If  right child isn't null, traverse left subtree
        if self.right is not None:
            self.right.inorder(datas)
        return datas
        

    # Insert
    # Adds a Node with the data in the appropriate spot
    # Time Complexity: O(n)
    def insert(self,data):
        # If no root exists, set the root to the value
        if not self.data:
            self.data = data
            return

        # If root data is the same as data, we don't want dupes so return
        if self.data == data:
            return
        
        # If data is less than root, move to left
        if data < self.data:
            # If left child exists, insert it
            if self.left:
                self.left.insert(data)
                return
            # If left child doesn't exist, create new node 
            # with data and set as left child
            self.left = BSTNode(data)
            return


        # If data is greater than root, move to right
        if data > self.data:
            # If right child exists, insert it
            if self.right:
                self.right.insert(data)
                return
            # If right child doesn't exists, create new node
            # with data and set as right child
            self.right = BSTNode(data)
        
        
    # Remove
    # Deletes Node with the data and adjusts the tree accordingly
    # Time Complexity: O(n)
    def remove(self,data):

        # If root is empty
        if self == None:
            return self

        # Find Node that we want to delete

        # If data less than root data, traverse left
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
            return self
        
        # If data greater than root data, traverse right
        if data > self.data:
            if self.right:
                self.right = self.right.remove(data)
            return self

        
        if self.right == None:
            return self.left

        if self.left == None:
            return self.right

        min_larger_node = self.right

        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        self.data = min_larger_node.data

        # Delete successor
        self.right = self.right.remove(min_larger_node.data)

        return self
            



    # Find
    # Checks if a Node with the data is in the tree
    # Returns True if exists, false if doesn't exist
    # Time Complexity: O(n)
    def find(self,data):
        # If Node data equals data, return true
        if self.data == data:
            return True

        # If data is less than root, move to left
        if data < self.data:
            # If left child doesn't exist, element is not in the tree
            if not self.left:
                return False
            # Recursive call
            return self.left.find(data)
            

        # If data is greater than root, move to right
        if data > self.data:
            # If right child doesn't exist, element is not in the tree
            if not self.right:
                return False
            # Recursive call
            return self.right.find(data)



# TESTS

bst = BSTNode()

# Insert Tests
bst.insert(2)
bst.insert(1)
bst.insert(4)
bst.insert(5)
bst.insert(3)

print('Expected Inorder Traversal: [1,2,3,4,5]')
print('Actual Inorder Traversal: ' + str(bst.inorder([])))

# Delete Tests
print('Deleted 5')
bst.remove(5)
print('Deleted 2')
bst.remove(2)

print('Expected Output: [1,3,4]')
print('Actual Output: ' + str(bst.inorder([])))

# Find Test
print('Is 5 in the BST? ' + str(bst.find(5)))
print('Is 4 in the BST? ' + str(bst.find(4)))

# Min Test
print('Expected Min Value: 1')
print('Actual Min Value: ' + str(bst.min()))

# Max Test
print('Expected Max Value: 4')
print('Actual Max Value: ' + str(bst.max()))




