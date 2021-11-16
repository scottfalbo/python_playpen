class Tree:
    def __init__(self, root = None) -> None:
        self.root = root
    
class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.counter = 0

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.counter +=1

    def dequeue(self):
        node = self.front
        self.front = self.front.next
        self.counter -= 1
        return node.value
