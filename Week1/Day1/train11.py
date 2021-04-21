''' 수식의 괄호 검사 (Stack) L31, L33, L36, L37, L39 '''

class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    S = ArrayStack()

    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in match :
            if S.isEmpty() :
                return False
            else :
                t = match[c]
                if t != S.pop() :
                    return False
    return S.isEmpty()

print(solution('A + B'))
print(solution('( a + b )'))
print(solution('{ ( a + b ) * c ]'))
print(solution('{ ( a + b ) * ( c - d ) }'))