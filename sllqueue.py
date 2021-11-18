# Queue using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def dequeue(self):
        if self.head == None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    def isEmpty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    def printQueue(self):
        if self.head == None:
            print("Queue is empty")
            return
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next
        print()
    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.data
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.printQueue()
print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())
print(q.isEmpty())

