class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, value):
        NewNode = Node(value)
        NewNode.next = self.head
        if (self.head is None):
            self.tail = self.head = NewNode
        else:
            self.head = NewNode

    def pushBack(self, value):
        NewNode = Node(value)
        if (self.tail is None) :
            self.tail = self.head = NewNode
        else:
            self.tail.next = NewNode
            self.tail = NewNode

    def remove(self, removeKey):
        currentNode = self.head
        prevNode = None
        while (currentNode is not None):
            if currentNode.data == removeKey:
                if prevNode is not None:
                    prevNode.next = currentNode.next
                    if self.tail == currentNode:
                        self.tail = prevNode
                else:
                    self.head = currentNode.next
                return
            prevNode = currentNode
            currentNode = currentNode.next

    def popFront(self):
        node = self.head
        if self.head:
            if (self.head == self.tail):
                self.head = self.tail = None
            else:
                self.head = self.head.next

            return node.data
        else:
            return None

    def popBack(self):
        node = self.tail
        if self.tail:
            if (self.head == self.tail):
                self.head = self.tail = None
            else:
                prevNode = None
                currentNode = self.head
                while (currentNode != self.tail):
                    prevNode = currentNode
                    currentNode = currentNode.next
                prevNode.next = None
                self.tail = prevNode
            return node.data
        else:
            return None

    def print(self):
        printVal = self.head
        while (printVal):
            print(printVal.data),
            printVal = printVal.next

if __name__ == '__main__':
    list = SinglyLinkedList()
    list.pushFront(4)
    list.pushFront(3)
    list.pushFront(2)
    list.pushFront(1)
    list.remove(4)
    list.popBack()
    list.popBack()
    list.popBack()
    list.print()
