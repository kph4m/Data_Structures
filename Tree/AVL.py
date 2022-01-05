# AVL TREE
# Self-balancing bst where each node has a balance factor of -1,0, or 1
# Applications
#   - Fast and efficient search times in large databases
#   - Data is mostly sorted

# Create Tree Node class, where each node has a key, left, right, and height property
class TreeNode(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# Create AVL Tree Class 
class AVL(object):

    # Insert
    # Time Complexity: O(logn) - searching for position of insertion and getting back to the root
    def insert(self, root, key):

        # FIND THE LOCATION TO INSERT NODE

        # Check if there's a root
        # If not, create new TreeNode with the key and return it
        if not root:
            return TreeNode(key)
        
        # If there is a root, check if key is less than or greater than the root

        # If key is less than root, insert on the left side
        elif key < root.key:
            root.left = self.insert(root.left, key)
        
        # If key is greater than root, insert on the right side
        elif key > root.key:
            root.right = self.insert(root.right, key)

        # UPDATE HEIGHT

        # Update the height of the tree using the getHeight function
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Update balance factors to make sure it fulfills reqs of AVL Tree
        balanceFactor = self.getBalanceFactor(root)

        # BALANCE THE TREE

        # If balance factor is greater than 1 (left side has greater than 1 difference in height between right side, where left side is greater than right side)
        if balanceFactor > 1:
            # Check if key is less than the key of the left child of root
            # If so, apply right rotate to the root
            if key < root.left.key:
                return self.rightRotate(root)

            # Else, perform a double rotate
            # Left rotate the left child of root and update it to the new left child
            # Right rotate the root
            else: 
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        # If balance factor is less than -1 (left side has greater than 1 difference in height between right side, where left side is less than right side)
        if  balanceFactor < -1:
            # Check if key is greater than the key of the right child of root
            # If so, apply left rotate to the root
            if key > root.right.key:
                return self.leftRotate(root)

            # Else, perform a double rotate
            # Right rotate the right child of root and update it to the new right child
            # Left rotate the root
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        
        
        # if there are no balance factor issues, return the root
        return root


    # Delete
    # Time Complexity: O(logn) - searching for node to be deleted and operations for balance factor
    def delete(self, root, key):

        # FIND THE NODE TO BE DELETED

        # If root doesn't exist, return root
        if not root:
            return root
        # if the key of the node is less than the root key, go left
        elif key < root.key:
            root.left = self.delete(root.left, key)
        # if the key of the node is greater than the root key, go right
        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,
                                          temp.key)
        if root is None:
            return root
        
        # UPDATE HEIGHT

        # Update the height of the tree using the getHeight function
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Update balance factors to make sure it fulfills reqs of AVL Tree
        balanceFactor = self.getBalanceFactor(root)

        # BALANCE TREE

        # If balance factor is greater than 1 (left side has greater than 1 difference in height between right side, where left side is greater than right side)
        if balanceFactor > 1:
            # Check if key is less than the key of the left child of root
            # If so, apply right rotate to the root
            if key < root.left.key:
                return self.rightRotate(root)

            # Else, perform a double rotate
            # Left rotate the left child of root and update it to the new left child
            # Right rotate the root
            else: 
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        # If balance factor is less than -1 (left side has greater than 1 difference in height between right side, where left side is less than right side)
        if  balanceFactor < -1:
            # Check if key is greater than the key of the right child of root
            # If so, apply left rotate to the root
            if key > root.right.key:
                return self.leftRotate(root)

            # Else, perform a double rotate
            # Right rotate the right child of root and update it to the new right child
            # Left rotate the root
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        # if there are no balance factor issues, return the root
        return root

    # Get the minimum value node in the tree (furthest left node)
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
        
    # Left Rotate
    # Time Complexity: O(1)
    def leftRotate(self, root):
        child1 = root.right
        child2 = child1.left
        child1.left = root
        root.right = child2

        # UPDATE HEIGHT
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        child1.height = 1 + max(self.getHeight(child1.left), self.getHeight(child1.right))

        return child1

    # Right Rotate
    # Time Complexity: O(1)
    def rightRotate(self,root):
        child1 = root.left
        child2 = child1.right
        child1.right = root
        root.left = child2

        # UPDATE HEIGHT
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        child1.height = 1 + max(self.getHeight(child1.left), self.getHeight(child1.right))

        return child1

    # Get Height
    def getHeight(self,root):
        # If root doesn't exist, return 0
        if not root:
            return 0
        return root.height

    # Get Balance Factor
    def getBalanceFactor(self,root):
        # If root doesn't exist, return 0
        if not root:
            return 0
        # Balance factor = height of left subtree - height of right subtree
        return self.getHeight(root.left) - self.getHeight(root.right)

    # Pre-order Traversal
    def preorder(self, root):
        # If root doesn't exist, return nothing
        if not root:
            return
        print(str(root.key) + " ", end="")
        self.preorder(root.left)
        self.preorder(root.right)


# TESTS

# Create AVLTree object
avlTree = AVL() 

# Initialize Root
root = None

# nums = [1,2,3,4,5,6]

# for num in nums:
#    root = avlTree.insert(root,num)

# Insert Nodes
print("Inserting 1 2 3 4 5 6")
root = avlTree.insert(root,1)
root = avlTree.insert(root,2)
root = avlTree.insert(root,3)
root = avlTree.insert(root,4)
root = avlTree.insert(root,5)
root = avlTree.insert(root,6)

print("Expected AVL Tree Output: 4 2 1 3 5 6")
print("Actual AVL Tree Output: ", end="")
avlTree.preorder(root)
print()

# Delete Nodes
print("Deleting 5")
root = avlTree.delete(root, 5)
print("Expected AVL Tree Output: 4 2 1 3 6")
print("Actual AVL Tree Output: ", end="")
avlTree.preorder(root)
print()

print("Deleting 2")
root = avlTree.delete(root, 2)
print("Expected AVL Tree Output: 4 3 1 6")
print("Actual AVL Tree Output: ", end="")
avlTree.preorder(root)