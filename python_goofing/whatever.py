from stuff.thing import Something
from stuff.tree import *

def hello():
    Something.do_something()
hello()

def make_tree():
    tree = Tree()
    node1 = Node(6)
    node2 = Node(5)
    node3 = Node(8)
    node4 = Node(4)
    node5 = Node(7)
    node6 = Node(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    tree.root = node1
    return tree

def add_leaves(tree):
    total = 0
    q = Queue()
    q.enqueue(tree.root)
    while q.front is not None:
        current = q.dequeue()
        total += current.value
        if current.left is not None:
            q.enqueue(current.left)
        if current.right is not None:
            q.enqueue(current.right)
    return total

tree = make_tree()
print(add_leaves(tree))
        

