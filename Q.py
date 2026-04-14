# n = int(input())
# k = int(input())
# prices = list(map(int, input().split()))

# s = set(prices)
# count = 0

# for price in prices:
#     if price + k in s:
#         count += prices.count(price + k)

# print(count)

###---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Create Node
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     # Insert
#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self.insertNode(self.root, value)

#     def insertNode(self, rootNode, value):
#         if value < rootNode.value:
#             if rootNode.left is None:
#                 rootNode.left = Node(value)
#             else:
#                 self.insertNode(rootNode.left, value)
#         else:
#             if rootNode.right is None:
#                 rootNode.right = Node(value)
#             else:
#                 self.insertNode(rootNode.right, value)

#     # Search
#     def search(self, value):
#         return self.searchNode(self.root, value)

#     def searchNode(self, rootNode, value):
#         if rootNode is None:
#             return False
#         if rootNode.value == value:
#             return True
#         if value < rootNode.value:
#             return self.searchNode(rootNode.left, value)
#         else:
#             return self.searchNode(rootNode.right, value)

#     # Vertical Print (sideways tree)
#     def printTree(self, rootNode, space=0):
#         if rootNode is None:
#             return

#         space += 5
#         self.printTree(rootNode.right, space)

#         print(" " * space + str(rootNode.value))

#         self.printTree(rootNode.left, space)


# # Create tree
# btObj = BinaryTree()

# btObj.insert(50)
# btObj.insert(30)
# btObj.insert(70)

# # Print Tree
# print("Tree Structure:")
# btObj.printTree(btObj.root)

# # Search
# print("\nSearch 30:", btObj.search(30))   # True
# print("Search 90:", btObj.search(90))   # False

####-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class BSTNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# def insertNode(rootNode, nodeValue):
#     if rootNode.data is None:
#         rootNode.data = nodeValue

#     elif nodeValue <= rootNode.data:
#         if rootNode.leftChild is None:
#             rootNode.leftChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.leftChild, nodeValue)

#     else:
#         if rootNode.rightChild is None:
#             rootNode.rightChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.rightChild, nodeValue)

#     return "The node has been successfully inserted"


# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     print(rootNode.data)
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)


# def inOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data)
#     inOrderTraversal(rootNode.rightChild)


# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data)


# # -------- MAIN --------
# newBST = BSTNode(None)

# insertNode(newBST, 70)
# insertNode(newBST, 50)
# insertNode(newBST, 90)
# insertNode(newBST, 30)
# insertNode(newBST, 60)
# insertNode(newBST, 80)
# insertNode(newBST, 100)
# insertNode(newBST, 20)
# insertNode(newBST, 40)

# print("Preorder:")
# preOrderTraversal(newBST)

# print("\nInorder:")
# inOrderTraversal(newBST)

# print("\nPostorder:")
# postOrderTraversal(newBST)

####--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Check for prime numbers in a range:
#Q. Write a function to find and return all prime numbers within a given range

# for num in range(1, 21):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")

####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Graph consists of a finite set of vertices (or nodes) and a set of edges which connect pair of nodes
#If a graph is complete or almost complete we should use ADJACENCY MATRIX
#If the number of edges are few then we should use ADJACENCY LIST
# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list:
#             self.adjacency_list[vertex] = []
#             return True
#         return False

#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ":", self.adjacency_list[vertex])


# # create graph object
# my_graph = Graph()

# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")

# # print graph
# my_graph.print_graph()


####-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list:
#             self.adjacency_list[vertex] = []

#     def add_edge(self, v1, v2):
#         # undirected graph without duplicates
#         if v1 in self.adjacency_list and v2 in self.adjacency_list:
#             if v2 not in self.adjacency_list[v1]:
#                 self.adjacency_list[v1].append(v2)
#             if v1 not in self.adjacency_list[v2]:
#                 self.adjacency_list[v2].append(v1)

#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ":", self.adjacency_list[vertex])


# # create graph
# g = Graph()

# # vertices
# for v in ["A", "B", "C", "D", "E", "F"]:
#     g.add_vertex(v)

# # edges (same as yours)
# g.add_edge("A", "B")
# g.add_edge("A", "C")

# g.add_edge("B", "D")
# g.add_edge("B", "E")

# g.add_edge("C", "A")
# g.add_edge("C", "E")

# g.add_edge("D", "B")
# g.add_edge("D", "E")
# g.add_edge("D", "F")

# g.add_edge("E", "C")
# g.add_edge("E", "D")
# g.add_edge("E", "F")

# g.add_edge("F", "D")
# g.add_edge("F", "E")

# g.print_graph()

######-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import datetime
# date = datetime.datetime.now()
# print("It's now:{:%d/%m/%Y %H:%M%S}".format(date))

#######------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

