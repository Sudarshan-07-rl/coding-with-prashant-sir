# =========================================================================================================================
# ========================================================================================================================

# Tree Data Structure
# tree is a non-linear data structure
# tree is a hierarchical data structure
# tree is a collection of nodes
# tree is a collection of edges
# tree is a collection of vertices
# tree is a collection of edges and vertices
# tree is a collection of nodes and edges
# tree is a collection of nodes and vertices
# tree is a collection of edges and vertices and nodes

# types of trees
# binary tree
# binary search tree
# AVL tree
# Red-Black tree
# B-tree
# B+ tree
# Splay tree
# Threaded binary tree
# Expression tree
# Trie (Prefix tree)
# Suffix tree
# Segment tree
# Fenwick tree (Binary indexed tree)
# Link/cut tree
# Tree diagram

# Tree Implemented by List
# Tree Implemented by Linked List
# Tree Implemented by Class
# Tree Implemented by Dictionary
# Tree Implemented by Set
# Tree Implemented by Tuple
# Tree Implemented by Array
# Tree Implemented by Stack
# Tree Implemented by Queue
# Tree Implemented by Heap
# Tree Implemented by Graph
# Tree Implemented by Tree
# Tree Implemented by Binary Tree
# Tree Implemented by Binary Search Tree
# Tree Implemented by AVL Tree
# Tree Implemented by Red-Black Tree
# Tree Implemented by B-Tree
# Tree Implemented by B+-Tree
# Tree Implemented by Splay Tree
# Tree Implemented by Threaded Binary Tree
# Tree Implemented by Expression Tree
# Tree Implemented by Trie (Prefix Tree)
# Tree Implemented by Suffix Tree
# Tree Implemented by Segment Tree
# Tree Implemented by Fenwick Tree (Binary Indexed Tree)
# Tree Implemented by Link/Cut Tree
# Tree Implemented by Tree Diagram

# Tree Functions
# Tree Traversal
# Tree Search
# Tree Insert
# Tree Delete
# Tree Update
# Tree Display
# Tree Height
# Tree Size
# Tree Level
# Tree Path
# Tree Diameter
# Tree Center
# Tree Radius
# Tree Eccentricity
# Tree Connectivity
# Tree Connectivity Matrix
# Tree Connectivity Vector
# Tree Connectivity Graph
# Tree Connectivity Tree
# Tree Connectivity Forest
# Tree Connectivity Graph
# Tree Connectivity Tree
# Tree Connectivity Forest

# Tree operations are :
#   - Insert
#   - Delete
#   - Search
#   - Traverse
#   - Update
#   - Display
#   - Height
#   - Size
#   - Level
#   - Path
#   - Diameter
#   - Center
#   - Radius
#   - Eccentricity
#   - Connectivity
#   - Connectivity Matrix
#   - Connectivity Vector
#   - Connectivity Graph
#   - Connectivity Tree
#   - Connectivity Forest

# =========================================================================================================================
# =========================================================================================================================

# Tree Implementation
# class Tree:
#     def __init__(self,data):
#         self.data = data
#         self.children = []

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret = " "*level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret

# rootNode = Tree("Drinks")
# hot           = Tree("Hot")
# cold          = Tree("Cold")
# tea           = Tree("Tea")
# coffee        = Tree("Coffee")
# non_alcoholic = Tree("Non-Alcoholic")
# alcoholic     = Tree("Alcoholic")

# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffee)
# cold.addChild(non_alcoholic)
# cold.addChild(alcoholic)

# print(rootNode)

# =========================================================================================================================
# =========================================================================================================================

# Binary Tree
# Each node can have at most 2 children or 0 children
# No nodes has a single child
# It Can be implemented by Array or Linked List
# It is a hierarchical data structure

# =========================================================================================================================

# Complete Binary Tree
# All levels are completely filled except possibly the last level
# Last level has all keys as left as possible

# All Levels except possibly the last level are completely filled
# Nodes in the last level are filled from left to right

# =========================================================================================================================

# Perfect Binary Tree
# All internal nodes have two children and all leaves are at the same level

# All internal nodes have exactly two children
# All leaf nodes are at the same level
# Number of nodes at each level doubles as we go down
# Total nodes = 2^h - 1 (where h is height)
# Height = log2(n+1)
# Maximum nodes at level l = 2^l
# Minimum nodes at level l = 2^(l-1)
# Maximum height = n (for skewed tree)
# Minimum height = log2(n+1)

# =========================================================================================================================

# Full Binary Tree
# Every node has 0 or 2 children

# All internal nodes have exactly two children
# All leaf nodes are at the same level
# Number of nodes at each level doubles as we go down
# Total nodes = 2^h - 1 (where h is height)
# Height = log2(n+1)
# Maximum nodes at level l = 2^l
# Minimum nodes at level l = 2^(l-1)
# Maximum height = n (for skewed tree)
# Minimum height = log2(n+1)

# =========================================================================================================================

# Balanced Binary Tree
# The height of the left and right subtrees of any node differs by at most 1

# The left and right subtrees are balanced
# The left and right subtrees are balanced
# The left and right subtrees are balanced

# =========================================================================================================================

# class Tree:
# class Tree:
#     def __init__(self,data):
#         self.data = data
#         self.children = []

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret = " "*level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret

# rootNode = Tree("N1")
# N2   = Tree("N2")
# N3   = Tree("N3")
# N4   = Tree("N4")
# N5   = Tree("N5")
# N6   = Tree("N6")
# N7   = Tree("N7")
# N9   = Tree("N9")
# N10  = Tree("N10")
# rootNode.addChild(N2)
# rootNode.addChild(N3)
# N2.addChild(N4)
# N2.addChild(N5)
# N3.addChild(N6)
# N3.addChild(N7)
# N4.addChild(N9)
# N4.addChild(N10)

# print(rootNode)

# =========================================================================================================================
# =========================================================================================================================

# Pre-order Traversal
# Root -> Left -> Right

# In-order Traversal
# Left -> Root -> Right

# Post-order Traversal
# Left -> Right -> Root

# =========================================================================================================================
# =========================================================================================================================

# traversing a tree

class Node:
    # create a node in the tree
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        # Insert root node in if block if there is no root node
        if self.root is None:
            self.root = Node(value)
        else :
            self.insertNode(self.root,value)

    def insertNode(self,rootNode,value):
        if value < rootNode.value:
            if rootNode.left is None:
                rootNode.left = Node(value)

            else:
                self.insertNode(rootNode.left,value)            # Recursive Call
             
        else:
            if rootNode.right is None:
                rootNode.right = Node(value)

            else:
                self.insertNode(rootNode.right,value)
                
        return rootNode
        
btObj = BinaryTree()
btObj.insert(50)
btObj.insert(30)
btObj.insert(70)

print(btObj)