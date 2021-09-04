# 0902 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81303

class Node :
    def __init__(self, item) -> None:
        self.item = item
        self.next = None
        self.prev = None

    def __repr__(self) :
        return str(self.item)

class LinkedList :
    def __init__(self, length) -> None:
        self.list = dict()
        self.list[-1] = Node(None)
        self.list[length] = Node(None)
        self.head = self.list[-1]
        self.tail = self.list[length]

        self.head.next = self.tail
        self.tail.prev = self.head
        self.full_length = length

    def __len__(self) :
        return len(self.list)-2

    def get_node(self, n) :
        return self.list[n]

    def insert(self, n) :
        new_node = Node(n)

        prev_node = self.get_node(n-1)

        prev_node.next.prev = new_node
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        
        self.list[n] = new_node

    def pop(self, n) :
        pop_node = self.get_node(n)

        pop_node.next.prev = pop_node.prev
        pop_node.prev.next = pop_node.next

        del(self.list[n])
        return pop_node

    def restore(self, re_node) :
        n = re_node.item

        prev_node = re_node.prev
        next_node = re_node.next

        prev_node.next = re_node
        next_node.prev = re_node

        self.list[n] = re_node

def solution(n, k, cmd) :
    db = LinkedList(n)

    for i in range(n) :
        db.insert(i)
    
    exists = [True for _ in range(n)]
    del_stack = []
    cursor = db.get_node(k)

    for commend in cmd :
        if commend[0] == 'U' :
            x = int(commend[2:])
            while x and cursor.prev != db.head :
                cursor = cursor.prev
                x -= 1
                
        elif commend[0] == 'D' :
            x = int(commend[2:])
            while x and cursor.next != db.tail :
                cursor = cursor.next
                x -= 1

        elif commend[0] == 'C' :
            del_node = db.pop(cursor.item)
            del_stack.append(del_node)
            exists[del_node.item] = False

            if cursor.next == db.tail :
                cursor = cursor.prev
            else :
                cursor = cursor.next

        elif commend[0] == 'Z' :
            re_node = del_stack.pop()
            db.restore(re_node)
            exists[re_node.item] = True
        '''
        print(commend)
        print(cursor.item, cursor.prev.item, cursor.next.item)
        print(del_stack)
        print(''.join(['O' if e else 'X' for e in exists]))
        '''
    return ''.join(['O' if e else 'X' for e in exists])

'''
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))

'''
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))

'''
n = 5
k = 2
cmd = ["D 2","D 2","D 2","D 2","D 2","C","U 3","Z"]
print(solution(n, k, cmd))
'''