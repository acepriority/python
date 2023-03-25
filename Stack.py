class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self, item):
        if len(self.stack) > 0:
            return self.stack.pop(item)
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else: 
            return None
            
    def __str(self):
        return str(self.stack)

my_stack = Stack()
my_stack.push(9)
my_stack.push(90)
my_stack.push(100)
my_stack.peek()
