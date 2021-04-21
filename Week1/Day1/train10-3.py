''' 양방향 연결 리스트 노드 삭제 L72 ~ L87 '''

class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        popNode = prev.next
        next = popNode.next

        prev.next = next
        next.prev = prev

        self.nodeCount -= 1
        return popNode.data

    def popBefore(self, next):
        popNode = next.prev
        prev = popNode.prev

        prev.next = next
        next.prev = prev

        self.nodeCount -= 1
        return popNode.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount :
            raise IndexError

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

def solution(x):
    return 0

L = DoublyLinkedList()

L.insertAt(1, Node(1))
L.insertAt(2, Node(15))
L.insertAt(1, Node(346))
L.insertAt(3, Node(23))
L.insertAt(2, Node(5))

print(L.traverse())
print(L.popAt(5))
print(L.traverse())