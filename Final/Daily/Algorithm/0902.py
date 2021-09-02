# 0902 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81303

class Node :
    def __init__(self, item) -> None:
        self.item = item
        self.next = None
        self.prev = None

class LinkedList :
    def __init__(self) -> None:
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def get_node(self, n) :
        if n > self.len / 2 :
            n = self.len - n + 1
            cur_node = self.tail

            for _ in range(n) :
                cur_node = cur_node.prev
        else :
            cur_node = self.head

            for _ in range(n) :
                cur_node = cur_node.next

        return cur_node

    def _insert(self, prev_node, item) :
        new_node = Node(item)

        new_node.prev = prev_node
        prev_node.next.prev = new_node

        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert(self, n, item) :
        prev_node = self.get_node(n-1)

        self._insert(prev_node, item)
        self.len += 1

    def _pop_next_node(self, prev_node) :
        del_node = prev_node.next

        del_node.next.prev = prev_node
        prev_node.next = del_node.next

        return del_node

    def pop(self, n) :
        prev_node = self.get_node(n-1)

        pop_node = self._pop_next_node(prev_node)
        self.len -= 1
        
        return pop_node


def solution(n, k, cmd) :
    answer = ''

    db = LinkedList()

    for i in range(n) :
        db.insert(i+1, i)
    
    exists = [True for _ in range(n)]
    del_stack = []
    cursor = k+1

    for commend in cmd :
        if commend[0] == 'U' :
            x = int(commend[2:])
            cursor = cursor - x if cursor >= x else 0
        if commend[0] == 'D' :
            x = int(commend[2:])
            cursor = cursor + x if cursor + x < db.len+1 else db.len
        if commend[0] == 'C' :
            del_stack.append((db.pop(cursor).item, cursor))
            exists[cursor-1] = False
        if commend[0] == 'Z' :
            item, idx = del_stack.pop()
            db.insert(idx-1, item)
            exists[idx-1] = True

    return ''.join(['O' if e else 'X' for e in exists])

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

print(solution(n, k, cmd))

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(n, k, cmd))