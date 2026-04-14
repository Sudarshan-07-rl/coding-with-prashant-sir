# # class Tree:
# #     def __init__(self, data):
# #         self.data = data 
# #         self.children = []
        
# #     def addChild(self, child):
# #         self.children.append(child)
        
# #     def __str__(self, level = 0):
# #         ret = "  "* level + str(self.data) + "\n"
# #         for child in self.children:
# #             ret += child.__str__(level + 1)
# #         return ret
        
# # #object creation:
# # rootNode = Tree("Drinks")
# # hot = Tree("Hot")
# # cold = Tree("Cold")
# # tea = Tree("Tea")
# # coffee = Tree("Coffee")
# # nonalcoholic = Tree("NonAlcohlic")
# # alcoholic = Tree("Alcoholic")

# # #add child nodes in tree:
# # rootNode.addChild(hot)
# # rootNode.addChild(cold)
# # hot.addChild(tea)
# # hot.addChild(coffee)
# # cold.addChild(nonalcoholic)
# # cold.addChild(alcoholic)

# # print(rootNode)

# ######---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # class Tree:
# #     def __init__(self,data):
# #         self.data = data
# #         self.children = []

# #     def addChild(self,child):
# #         self.children.append(child)

# #     def __str__(self,level=0):
# #         ret = " "*level + str(self.data) + "\n"
# #         for child in self.children:
# #             ret += child.__str__(level+1)
# #         return ret

# # rootNode = Tree("N1")
# # N2   = Tree("N2")
# # N3   = Tree("N3")
# # N4   = Tree("N4")
# # N5   = Tree("N5")
# # N6   = Tree("N6")
# # N7   = Tree("N7")
# # N9   = Tree("N9")
# # N10  = Tree("N10")
# # rootNode.addChild(N2)
# # rootNode.addChild(N3)
# # N2.addChild(N4)
# # N2.addChild(N5)
# # N3.addChild(N6)
# # N3.addChild(N7)
# # N4.addChild(N9)
# # N4.addChild(N10)

# # print(rootNode)

# ####--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class Node:
#     #create a node inthe tree
#     def __init__(self, value):
#         self.value = value #value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#          self.root = None

#     def insertNode(self,rootNode, value): #value =70
#         if value < rootNode.value: #70 < 50
#             #inserting node in the left and right position
#             if rootNode.left is None:
#                 rootNode.left = Node(value)
#             else:
#                 self.insertNode(rootNode.left, value) #recursive call
#         else:
#             if rootNode.right is None:
#                 rootNode.right = Node(value) #(70)
#             else:
#                 self.insertNode(rootNode.left, value)                   

            

# btObj = BinaryTree()
# btObj.insert(50) 
# btObj.insert(30)
# btObj.insert(70)

# print(Obj)