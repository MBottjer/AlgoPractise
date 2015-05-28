class Stack:

    # intialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        # if the stack is empty, return None
        if not self.items: return None

        return self.items[len(self.items)-1]

class MaxStack:

    def __init__(self):
        self.stack      = Stack()
        self.maxs_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if item >= self.maxs_stack.peek()
            self.maxs_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.maxs_stack.peek():
            self.maxs_stack.pop()
        return item

    def get_max(self):
        return self.maxs_stack.peek()