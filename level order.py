class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def level_order(root):
    queue=[root]
    while(len(queue)):
        l=[]
        for i in range(len(queue)):
            element=queue.pop(0)
            print(element.data,end=" ")
            l.append(element)
        print()
        for i in l:
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
root=Node(2)
root.left=Node(7)
root.right=Node(5)
root.left.left=Node(2)
root.left.right=Node(6)
root.right.right=Node(9)
root.left.right.left=Node(5)
root.left.right.right=Node(11)
root.right.right.left=Node(4)
level_order(root)
