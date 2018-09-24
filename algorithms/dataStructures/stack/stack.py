class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if len(self.stack) else None

if __name__ == '__main__':
    stack = Stack()
    stack.push("Mon")
    stack.push("Tue")
    print(stack.pop())
    stack.push("Wed")
    stack.push("Thu")
    print(stack.pop())
