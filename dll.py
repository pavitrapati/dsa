# Doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublylinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = cur
            cur = cur.next
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    self.head = None
                    cur = None
                    return
                else:
                    nxt = cur.next
                    nxt.prev = None
                    cur.next = None
                    cur = None
                    return
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next
    def delete_end(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.prev.next = None
        cur.prev = None
        cur = None
    def search(self, key):
        cur = self.head
        while cur:
            if cur.data == key:
                return True
            cur = cur.next
        return False
dll=DoublylinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.print_list()
dll.prepend(0)
dll.add_after_node(3,6)
dll.delete(4)
dll.delete_end()
dll.print_list()
print(dll.search(5))    