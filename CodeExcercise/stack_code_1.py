class stack():
    def __init__(self):
        self.items=[]
    def push(self,items):
        return self.items.append(items)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items==[]
    def peek(self):
        return self.items(len(self.items-1))
    def get_stack(self):
        return self.items
mystack=stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.pop()
print(mystack.peek())
print(mystack.get_stack())
print(mystack.isEmpty())