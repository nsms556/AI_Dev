class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def bft(self):
        tr = []

        if self.root :
            trQ = ArrayQueue()
            trQ.enqueue(self.root)

            while not trQ.isEmpty() :
                cursor = trQ.dequeue()
                tr.append(cursor.data)

                if cursor.left :
                    trQ.enqueue(cursor.left)
                if cursor.right :
                    trQ.enqueue(cursor.right)

        return tr


def solution(x):
    return 0

a = BinaryTree(Node(1))
a.root.left = Node(2)
a.root.right = Node(3)
a.root.left.right = Node(5)

print(a.bft())