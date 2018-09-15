import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from binarySearchTree import Node, initTree

class TraversedNode(Node):
    def inOrderTraverse(self):
        if self.left:
            self.left.inOrderTraverse()
        print(self.data)
        if self.right:
            self.right.inOrderTraverse()

if __name__ == '__main__':
    root = initTree(TraversedNode)
    root.inOrderTraverse()

