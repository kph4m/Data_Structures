# Red Black Tree
# Self-balancing tree that contains information denoting the color of the node (Black/Red)
# Properties
#   - Each node is red or black
#   - Root is black
#   - Every leaf is black
#   - Red node's children are black
#   - Each node has the same number of black nodes to get to a descendant leaf

# Create node
class Node():
    def __init__(self, data):
        # Set to red
        self.color = 1
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


# Create RBTree Class
class RBTree():
    # Set default values
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = 0
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil


    # Insert
    def insert(self, data):

        # Create new node
        new_node = Node(data)

        # Set parent
        new_node.parent = None

        # Set left child
        new_node.left = self.nil

        # Set right child
        new_node.right = self.nil

        # Set color to red by default
        new_node.color = 1

        # BST insertion
        parent = None
        current = self.root
        while current != self.nil:
            # If  less than, move to left
            if new_node.data < current.data:
                current = current.left

            # If greater than, move to right
            if new_node.data > current.data:
                current = current.right

        # insert node
        # If no parent, set as root
        if parent == None:
            self.root = new_node
        # if new node is greater than parent, set to left
        elif new_node.data > parent.data:
            parent.left = new_node
        else:
            parent.right = new_node


    # Rotate left
    def rotateLeft(self, x):
        y = x.right
        x.right = y.left

        # if left child of y not a leaf, set y parent to x
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Rotate right
    def rotateRight(self,x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Fix Insert
    # Maintains property of rb tree after insertion
    def fix_insert(self, k):
        # while parent is red
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                # if color of left child of grandparent red
                if u.color == 1:
                    # set the children of grandparent to black
                    u.color = 0
                    k.parent.color = 0
                    # set color of grandparent red
                    k.parent.parent.color = 1
                    # set new node to grandparent
                    k = k.parent.parent
                else:
                    # if left child of parent is the new node
                    if k == k.parent.left:
                        # set new node to parent
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                # if color of right child of grandparent red
                if u.color == 1:
                    # set children of grandparent black
                    u.color = 0
                    k.parent.color = 0
                    # set grandparent red
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    # if right child of parent is the new node
                    if k == k.parent.right:
                        # set new node to parent
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0


