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

def initTree(nodeCreator):
    A = nodeCreator("A")
    B = nodeCreator("B")
    C = nodeCreator("C")
    D = nodeCreator("D")
    E = nodeCreator("E")
    K = nodeCreator("K")
    L = nodeCreator("L")
    M = nodeCreator("M")
    N = nodeCreator("N")
    O = nodeCreator("O")
    P = nodeCreator("P")
    R = nodeCreator("R")
    S = nodeCreator("S")
    A.left = B
    A.right = M
    B.left = C
    B.right = E
    C.right = D
    E.left = K
    E.right = L
    M.left = N
    M.right = O
    O.right = P
    P.left = R
    P.right = S
    return A

if __name__ == '__main__':
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)

    root.find(3)
    print(root.find(33))
