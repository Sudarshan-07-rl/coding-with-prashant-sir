import sys

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class  LinkedList:
    def __init__(self):
        self.head = None

    def addnode(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def addNodeinBeginning(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addNodeinBetween(self, value, left_value, right_value):
        if self.head is None:
            print("List is empty. Cannot insert between nodes.")
            return

        current = self.head
        while current is not None:
            if current.data == left_value and current.next is not None and current.next.data == right_value:
                new_node = node(value)
                new_node.next = current.next
                current.next = new_node
                if current is self.tail:
                    self.tail = new_node
                return
            current = current.next

        print(f"No adjacent nodes found with values {left_value} and {right_value}. Cannot insert {value} between them.")

    def addNodeatEnd(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    obj = LinkedList()

    while True:
        print("\n1. Add Node in Linked List :")
        print("2. Add node in Beginning :")
        print("3. Add node Between  :")
        print("4. Add node at End :")
        print("5. Display Linked List :")
        print("6. Exit")
        
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            val = int(input("Enter value for node : "))
            obj.addnode(val)
        elif choice == 2:
            val = int(input("Enter value for node : "))
            obj.addNodeinBeginning(val)
        elif choice == 3:
            val = int(input("Enter value for node : "))
            left_val = int(input("Enter the value of the node before the new node: "))
            right_val = int(input("Enter the value of the node after the new node: "))
            obj.addNodeinBetween(val, left_val, right_val)
            print("Element Added Successfully")
        elif choice == 4:
            val = int(input("Enter value for node : "))
            obj.addNodeatEnd(val)
        elif choice == 5:
            obj.display()
        elif choice == 6:
            obj.exit()