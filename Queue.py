#Queue implementation with size limit
import sys #importing sys module

class Queue:#Queue class
    def __init__(self, QueueSize):# parameterized constructor
        self.queueList = [] #Queue creation
        self.queueSize = QueueSize

    def isFull(self):
        if len(self.queueList) == self.queueSize:#Checking if the queue is full
            return True
        else:
            return False
    
    def Enqueue(self, value):# add Element to queue operation
        if self.isFull():
            print("Queue is full")
        else:
            self.queueList.append(value)

    def displayQueue(self):#Display queue elements operation
        print("==========================================")
        print(self.queueList)
        print("==========================================")

    def isEmpty(self):#isEmpty operation
        if self.queueList == []:#Checking if the queue is empty
            return True
        else:
            return False

    def Dequeue(self):#remove Element from queue operation
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.queueList.pop(0)

    def deleteQueue(self):#Delete queue operation
        self.queueList = []

    def peek(self):# returns 1st element of queue
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.queueList[0]

    def exit(self):#Exit operation
        print("Exiting...")
        exit()

size = int(input("Enter the size of the Queue : "))
Queueobj = Queue(size)#Queue object creation

while True:#Main loop
    print("1. Enqueue Element in Queue :")
    print("2. Display Queue Elements :")
    print("3. Check if Queue is empty :")
    print("4. Dequeue Element from Queue :")
    print("5. Delete Queue :")
    print("6. Peek Element from Queue :")
    print("7. Exit")
    
    
    chioce = int(input("Enter your choice : "))#User choice
    if chioce == 1:#Push operation
        val = int(input("Enter value in Queue : "))
        Queueobj.Enqueue(val)#Push operation
        if Queueobj.isFull():
            print("You can't add more elements")
    
    elif chioce == 2:#Display operation
        Queueobj.displayQueue()
    
    elif chioce == 3:#isEmpty operation
        print(Queueobj.isEmpty())
    
    elif chioce == 4:# Dequeue operation
        print(Queueobj.Dequeue())
    
    elif chioce == 5:#Delete queue operation
        Queueobj.deleteQueue()
        print("Queue deleted successfully")
    
    elif chioce == 6:#Peek operation
        print("First element of queue is : ", Queueobj.peek())
    
    elif chioce == 7:#Exit operation
        Queueobj.exit()
