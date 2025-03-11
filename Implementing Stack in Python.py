class Stack:

    def __init__(self):
        self.stack_list = []
    
    def push(self, data):
        self.stack_list.append(data)
    
    def pop(self):
        stack_list_length = len(self.stack_list)
        self.stack_list = self.stack_list[:stack_list_length-1]
    
    def top(self):
        return self.stack_list[-1]
    
    def size(self):
        return len(self.stack_list)
    
    def empty(self):
        return len(self.stack_list) == 0


stk = Stack()
stk.push(2)
stk.push(3)
stk.push(2)
stk.push(1)
print(stk.top())
print(stk.size())
print(stk.empty())
stk.pop()
print(stk.top())
print(stk.size())

    
