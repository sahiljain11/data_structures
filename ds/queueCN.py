class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def enqueue(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def dequeue(self):
        if self.head == None:               #If queue empty
            print("poopoo da que empty")
            return
        if self.head.next != None:          #If queue has more than one element
            self.head = self.head.next
            self.head.prev = None
            return
        self.head = None                    #If queue has one element
        self.tail = None

    def print_queue(self):                #Queue printing function
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next
        print("")


qu = Queue()
qu.enqueue(2)
qu.enqueue(7)
qu.enqueue(3)
qu.print_queue()

qu.dequeue()
qu.print_queue()

qu.dequeue()
qu.print_queue()


qu.dequeue()
qu.print_queue()


qu.dequeue()
qu.print_queue()

    

            


