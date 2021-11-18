# binary search tree implementation in python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        root = Node(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
k=0
while True:
    print("1.insert 2.inorder 3.preorder 4.postorder 5.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        if k==0:
            data=int(input("enter the head value: "))
            root=Node(data)
            k+=1
        else:
            data=int(input("enter the value: "))
            root = insert(root,data)
    elif choice==2:
        inorder(root)
    elif choice==3:
        preorder(root)
    elif choice==4:
        postorder(root)
    elif choice==5:
        break
