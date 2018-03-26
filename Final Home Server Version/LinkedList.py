class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def add(self, key):
        node = Node(key)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def printList(self):
        cNode = self.head

        x = 0
        while(cNode != None):
            print("     " + str(x) + ": " + str(cNode.key))
            cNode = cNode.next
            x = x + 1

        x = 0