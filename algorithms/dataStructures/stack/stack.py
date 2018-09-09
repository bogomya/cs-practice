class Stack:

    def __init__(self):
        self.stack = []

    def push(self, dataval):
        self.stack.append(dataval)

    def pop(self):
        return self.stack.pop() if len(self.stack) else None

stack = Stack()
stack.push("Mon")
stack.push("Tue")
print(stack.pop())
stack.push("Wed")
stack.push("Thu")
print(stack.pop())
