# Implementation of singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insertafternode(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def postpend(self, data):
        new_node = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deletefirstnode(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deletelastnode(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next.next:
            last = last.next
        last.next = None

    def deleteafternode(self, prev_node):
        if not prev_node:
            print("Previous node is not in the list")
            return
        prev_node.next = prev_node.next.next

    def deletebeforenode(self, next_node):
        if not next_node:
            print("Next node is not in the list")
            return
        prev_node = self.head
        while prev_node.next != next_node:
            prev_node = prev_node.next
        prev_node.next = next_node

    def deleteatindex(self, index):
        if index == 0:
            self.deletefirstnode()
            return
        count = 0
        prev_node = self.head
        while count != index:
            prev_node = prev_node.next
            count += 1
        prev_node.next = prev_node.next.next

    def lenght(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

llist=linkedlist()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.prepend(0)
llist.postpend(6)
llist.insertafternode(llist.head.next, 7)
llist.printlist()
llist.deletefirstnode()
llist.lenght()
llist.printlist()
