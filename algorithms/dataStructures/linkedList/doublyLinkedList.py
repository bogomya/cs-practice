class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Add elements at the beginning
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def insert(self, prevNode, value):
        if prevNode is None:
            return
        newNode = Node(value)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if newNode.next is not None:
            newNode.next.prev = newNode

    # Add elements at the end
    def append(self, value):
        newNode = Node(value)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    def print(self, node):
        while (node is not None):
            print(node.data),
            node = node.next

if __name__ == '__main__':
    list = DoublyLinkedList()
    list.push(12)
    list.append(9)
    list.push(8)
    list.push(62)
    list.append(45)
    list.print(list.head)

