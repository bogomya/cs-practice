import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from binarySearchTree import Node, initTree


class BreadthTraversedNode(Node):
    def traverse(self):
        result = []
        queue = [self]
        while(len(queue)):
            node = queue.pop()
            result.append(node.data)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return result

if __name__ == '__main__':
    root = initTree(BreadthTraversedNode)
    print("breadthTraverse", root.traverse())
