class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.top = -1

    def push(self, item):
        if self.is_full():
            return ("Stack Overflow")
        self.stack.append(item)
        self.top += 1
        
    def pop(self):
        if self.is_empty():
            return ("Stack is empty")
        item = self.stack.pop()
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            return ("Stack is empty")
        return self.stack[self.top]
    
    def is_full(self):
        return self.size() == self.capacity 
    
    def is_empty(self):
        return self.top == -1
    
    def size(self):
        return self.top + 1

s = Stack(5)
for i in range(1, 6):
    s.push(i)

print("Is empty?", s.is_empty())
print("Size after push:", s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())