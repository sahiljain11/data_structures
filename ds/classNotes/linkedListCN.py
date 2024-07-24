class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.last = None
        self.head = None
    
    def addNode(self,data):
        newNode = Node(data)
        if self.head == None: #if linkedList is empty
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode
    
    def insertNode():
        #sahilList.insertNode(2,27)
        # 5, 3, 2, -247
        #       *
        # 5, 3, 27, 2, -247

        pass
    
    def deleteNode():
        #for this example dw bout duplicates
        #sahilList.del(7)
        # 5, 3, 7, -247
        # 5, 3, -247

        pass
    
    def printList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.next

            




sahilList = LinkedList()
sahilList.addNode(5)
sahilList.addNode(3)
sahilList.addNode(2)
sahilList.addNode(-247)
sahilList.printList()