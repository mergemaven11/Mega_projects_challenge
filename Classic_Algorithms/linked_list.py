class Node: 
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # Traversing a Linked List and print results
    def listprint(self):
        printli = self.head
        while printli is not None:
            print(printli.data)
            printli = printli.next

    # Add new node at start of list (Head)
    def newNodeAtHead(self, newitem):
        NewNode = Node(newitem)

        # Move items down to fit the New Item at head
        NewNode.next = self.head
        self.head = NewNode

bucketList = LinkedList()

bucketList.head = Node("Wine tasting")

nI2 = Node("Roller Coaster")
nI3 = Node("Sky Dive")
nI3 = Node("Wine taste")
nI4 = Node("Visit Tokyo")
nI5 = Node("Visit England")

bucketList.head.next = nI2

nI2.next = nI3
nI3.next = nI4
nI4.next = nI5

# Add new item at the beginning
bucketList.newNodeAtHead("Go fishing on a boat")

bucketList.listprint()



