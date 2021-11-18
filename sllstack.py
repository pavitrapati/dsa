# stack using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data
    def isEmpty(self):
        return self.head is None
    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    def printStack(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print()
st=Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.printStack()
print(st.peek())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.isEmpty())
st.printStack()