import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from binarySearchTree import Node

class TraversedNode(Node):
    def preOrderTraverse(self):
        print(self.data)
        if self.left:
            self.left.preOrderTraverse()
        if self.right:
            self.right.preOrderTraverse()

    def inOrderTraverse(self):
        if self.left:
            self.left.inOrderTraverse()
        print(self.data)
        if self.right:
            self.right.inOrderTraverse()

    def postOrderTraverse(self):
        if self.left:
            self.left.postOrderTraverse()
        if self.right:
            self.right.postOrderTraverse()
        print(self.data)

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
    root = initTree(TraversedNode)
    print("inOrderTraverse")
    root.inOrderTraverse()
    print("preOrderTraverse")
    root.preOrderTraverse()
    print("postOrderTraverse")
    root.postOrderTraverse()



