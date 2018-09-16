import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from binarySearchTree import Node

class TraversedNode(Node):
    def preOrderTraverse(self):
        result = []
        result.append(self.data)
        if self.left:
            result = result + self.left.preOrderTraverse()
        if self.right:
            result = result + self.right.preOrderTraverse()
        return result

    def iterativePreOrderTraverse(self):
        result = []
        stack = [self]
        while(len(stack) > 0):
            node = stack.pop()
            result.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def inOrderTraverse(self):
        result = []
        if self.left:
            result = self.left.inOrderTraverse()
        result.append(self.data)
        if self.right:
            result = result + self.right.inOrderTraverse()
        return result

    def iterativeInOrderTraverse(self):
        result = []
        stack = []
        node = self
        while(len(stack) or node != None):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right
        return result

    def postOrderTraverse(self):
        result = []
        if self.left:
            result = self.left.postOrderTraverse()
        if self.right:
            result = result + self.right.postOrderTraverse()
        result.append(self.data)
        return result

    def iterativePostOrderTraverse(self):
        result = []
        stack = []
        lastVisitedNode = None
        node = self
        while (len(stack) or node != None):
            if node:
                stack.append(node)
                node = node.left
            else:
                topNode = stack[-1]
                if topNode.right != None and lastVisitedNode != topNode.right:
                    node = topNode.right
                else:
                    result.append(topNode.data)
                    lastVisitedNode = stack.pop()
        return result

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
    print("preOrderTraverse", root.preOrderTraverse())
    print("iterativePreOrderTraverse", root.iterativePreOrderTraverse())
    print("inOrderTraverse",  root.inOrderTraverse())
    print("iterativeInOrderTraverse",  root.iterativeInOrderTraverse())
    print("postOrderTraverse", root.postOrderTraverse())
    print("iterativePostOrderTraverse", root.iterativePostOrderTraverse())




