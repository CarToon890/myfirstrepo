class Stack:
    
    def push(self, item):
        if self.is_full():
            raise Exception("Stack Overflow")
        self.stack.append(item)
        self.top += 1
        
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        item = self.stack.pop()
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def size(self):
        return self.top + 1
    
print("Size after push:",Stack.size())
print("Top element:",Stack.peek())

print("Pop:",Stack.pop())
print("Pop:",Stack.pop())
print("Pop:",Stack.pop())
print("Pop:",Stack.pop())
print("Pop:",Stack.pop())

print("Is empty:",Stack.is_empty())
print("Pop from empty:",Stack.pop())