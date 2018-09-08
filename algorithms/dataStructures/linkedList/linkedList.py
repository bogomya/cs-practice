class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def unshift(self, value):
        NewNode = Node(value)
        NewNode.next = self.head
        self.head = NewNode

    def remove(self, removeKey):
        currentNode = self.head
        prevNode = None
        while (currentNode is not None):
            if currentNode.data == removeKey:
                if prevNode is not None:
                    prevNode.next = currentNode.next
                else:
                    self.head = currentNode.next
                return
            prevNode = currentNode
            currentNode = currentNode.next

    def printList(self):
        printVal = self.head
        while (printVal):
            print(printVal.data),
            printVal = printVal.next


list = SinglyLinkedList()
list.unshift(4)
list.unshift(3)
list.unshift(2)
list.unshift(1)
list.remove(4)
list.printList()
