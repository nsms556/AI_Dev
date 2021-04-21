''' Dummy head를 가지는 연결 리스트 노드 삭제 L53 ~ L72 '''

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        popNode = prev.next

        if popNode == None :
            return None

        if popNode.next == None :
            self.tail = prev

        prev.next = popNode.next
        self.nodeCount -= 1
        return popNode.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount :
            raise IndexError

        prevNode = self.getAt(pos - 1)

        return self.popAfter(prevNode)

def solution(x):
    return 0