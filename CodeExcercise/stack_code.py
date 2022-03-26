from pythonds.basic import Stack
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,items):
        return self.append(items)
    def pop(self):
        return self.items
    def peek(self):
        return self.items(len(self.items-1))
    def size(self):
        return len(self.items)

    s = Stack()

    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())