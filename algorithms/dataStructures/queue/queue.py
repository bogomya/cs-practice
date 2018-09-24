import sys
sys.path.append('../')
from linkedList.linkedList import SinglyLinkedList

class Queue:
  def __init__(self):
      self.queue = []

  def push(self, value):
      self.queue.insert(0,value)
  def pop(self):
      return self.queue.pop() if len(self.queue) else None;


class LLQueue:
    def __init__(self):
        self.queue = SinglyLinkedList()
    def enqueue(self, value):
        self.queue.pushBack(value)
    def dequeue(self):
        return self.queue.popFront()

if __name__ == '__main__':
    queue = Queue()
    queue.push("Mon")
    queue.push("Tue")
    queue.push("Wed")
    print(queue.pop())
    print(queue.pop())

    queue = LLQueue()
    queue.enqueue("Mon")
    queue.enqueue("Tue")
    queue.enqueue("Wed")
    print(queue.dequeue())
    print(queue.dequeue())
