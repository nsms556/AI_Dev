# 0902 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81303

class Node :
    def __init__(self, key) -> None:
        self.key = key
        self.prev = None
        self.next = None

class LinkedList :
    def __init__(self) -> None:
        self.list = dict()

    def __len__(self) :
        return len(self.list)

    def get_node(self, n) :
        return self.list[n]

    def insert(self, n) :

        new_node = Node(n)
        self.list[n] = new_node
            
        prev_node.next.prev = new_node
        new_node.prev = prev_node

        new_node.next = prev_node.next.next
        prev_node.next = new_node

    def pop(self, n) :
        prev_node = self.get_node(n-1)
        del_node = self.get_node(n)

        
        del_node.next.prev = prev_node
        prev_node.next = del_node.next
        
        return del_node

def solution(n, k, cmd) :
    answer = ''

    db = LinkedList()
    exists = [True for _ in range(n)]
    del_stack = []
    cursor = k

    db.list[0] = Node(0)
    db.list[n-1] = Node(n-1)

    db.get_node(0).next = db.get_node(n-1)
    db.get_node(n-1).prev = db.get_node(0)

    for i in range(1, n-1) :
        db.insert(i)
        
    for commend in cmd :
        if commend[0] == 'U' :
            for _ in range(int(commend[2:])) :
                cursor = db.get_node(cursor).prev.key
                
        if commend[0] == 'D' :
            for _ in range(int(commend[2:])) :
                cursor = db.get_node(cursor).next.key
                
        if commend[0] == 'C' :
            node = db.pop(n)
            exists[cursor] = False
            
            if node.next == None :
                cursor = node.prev.key
            else :
                cursor = node.next.key

            del_stack.append((node, cursor))

        if commend[0] == 'Z' :
            node, idx = del_stack.pop()
            exists[idx] = True

            db.insert(node.key)

    return ''.join(['O' if e else 'X' for e in exists])

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

print(solution(n, k, cmd))

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

print(solution(n, k, cmd))


'''
pop(n) :
    del_node = get_node(n)

    if n == len(db)-1 :
        del_node.prev.next = del_node.next
    elif n == 0 :
        del_node.next.prev = del_node.prev
    else :
        del_node.prev.next = del_node.next
        del_node.next.prev = del_node.prev

    del(db[n])
    return del_node

insert(n) :
    new_node = stack.pop()

    if new_node.key == len(db)-1 :
        new_node.next = None
        
        get_node[key-1].next = new_node
    new_node.prev.next = new_node



'''