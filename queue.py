# Array implementation of queue
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
obj = Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print(obj.size())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.size())
print(obj.isEmpty())

