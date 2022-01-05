# B Tree
# Self-balancing tree where each node can:
#   - contain more than one key
#   - have more than one children
# Uses
#   - store multiple keys in a node = smaller height =  minimize disk access = faster
# TODO: Finish implementation when I understand it better

# Create B node
class BNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

# Tree
class Tree:
    def __init__(self,t):
        self.root = BNode(True)
        self.t = t

    # Insert Node with data
    def insert(self,data):
        


