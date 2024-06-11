class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) >= self.limit:
            print("Warning: Stack overflow")
        else:
            self.items.append(item)

            
    def pop(self):
        if self.isEmpty():
            return None  
        else:
            return self.items.pop()

    def peek(self):
        pass
        
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            return len(self.items) - self.items.index(target) - 1
        except ValueError:
            return -1
