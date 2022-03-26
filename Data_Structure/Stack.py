# Stack follow LIFO-Last in First Out
#Linear data structure

#Stack Operation#
# Push: Add an element to the top of a stack
# Pop: Remove an element from the top of a stack
# IsEmpty: Check if the stack is empty
# IsFull: Check if the stack is full
# Peek: Get the value of the top element without removing it



# Before pushing, we check if the stack is already full
# Before popping, we check if the stack is already empty

# /////Code/////

#creating a stack
def create_stack():
    stack=[]
    return stack;

#check empty stack
def check_empty(stack):
    return len(stack)==0;

#add item to stack
def AddItem(stack,item):
    stack.append(item)
    print("Add items to the stack: "+item)

#pop elements
def PopItem(stack):
    if(check_empty(stack)):
        return "Stack is empty"
    return stack.pop()


stack = create_stack()
AddItem(stack,str(1))
AddItem(stack,str(2))
AddItem(stack,str(3))

print("Pop element: "+PopItem(stack))