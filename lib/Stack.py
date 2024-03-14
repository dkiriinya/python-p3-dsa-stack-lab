class Stack:
    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack overflow")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack underflow")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            top_of_stack = len(self.items) - 1
            index = self.items.index(target)
            if top_of_stack - index == 0:
                return 0
            return top_of_stack - index
        except ValueError:
            return -1
