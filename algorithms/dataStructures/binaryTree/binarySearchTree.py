class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.find(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.find(lkpval)
        else:
            print(str(self.data) + ' is found')

    def print(self):
        if self.left:
            self.left.print()
        print(self.data),
        if self.right:
            self.right.print()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.print()

root.find(3)
print(root.find(33))
