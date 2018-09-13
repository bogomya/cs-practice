class Queue:
  def __init__(self):
      self.queue = []

  def push(self, dataval):
      self.queue.insert(0,dataval)
  def pop(self):
      return self.queue.pop() if len(self.queue) else None;

queue = Queue()
queue.push("Mon")
queue.push("Tue")
queue.push("Wed")
print(queue.pop())
print(queue.pop())
