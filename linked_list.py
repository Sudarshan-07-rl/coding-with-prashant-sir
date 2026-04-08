#=========================================================================
# Linked List Implementation
#=========================================================================

# class Node: # Node class
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList: # Linked List class
#     def __init__(self):
#         self.head = None

# # Creating nodes
# linkedlist = LinkedList()
# linkedlist.head = Node(5)
# second = Node(10)
# third = Node(15)
# fourth = Node(20)

# # Linking part : Link the nodes
# linkedlist.head.next = second
# second.next = third
# third.next = fourth

# # Displaying the linked list
# while linkedlist.head:
#     print("|",linkedlist.head.data,"|","->",linkedlist.head.next,"|",end="  ")
#     linkedlist.head = linkedlist.head.next

#=========================================================================
#=========================================================================

# menu driven linked list

#=========================================================================
#=========================================================================

#==>>
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
    
    def display(self):
        while self.head:
            print("|",self.head.data,"|","->",self.head.next,"|",end="  ")
            self.head = self.head.next
    
    def delete(self, data):
        while self.head:
            if self.head.data == data:
                self.head = self.head.next
                break
            self.head = self.head.next

    def search(self, data):
        while self.head:
            if self.head.data == data:
                return True
            self.head = self.head.next
        return False
 
ll = LinkedList()

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Delete")
    print("4. Search")
    print("5. Exit")
        
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data: "))
        ll.insert(data)
    elif choice == 2:
        ll.display()
    elif choice == 3:
        data = int(input("Enter data: "))
        ll.delete(data)
    elif choice == 4:
        data = int(input("Enter data: "))
        print(ll.search(data))
    elif choice == 5:
        sys.exit(0)
    else:
        print("Invalid choice")