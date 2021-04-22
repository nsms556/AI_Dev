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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for c in S :
        print(c)
        if c in prec :
            if c == '(' :
                opStack.push(c)
            else :
                if opStack.isEmpty() :
                    opStack.push(c)
                else :
                    while opStack.size() > 0 :
                        if prec[opStack.peek()] >= prec[c] :
                            answer += '{}'.format(opStack.pop())
                        else :
                            break
                    opStack.push(c)
        elif c == ')' :
            while not opStack.isEmpty() :
                t = opStack.pop()
                if t == '(' :
                    break
                else :
                    answer += '{}'.format(t)
        else :
            answer += '{}'.format(c)
            
    while not opStack.isEmpty() :
        answer += '{}'.format(opStack.pop())
            
    return answer

a = '(A+(B-C))*D'
b = 'A*(B-(C+D))'
c = "(A+B)*(C+D)"
d = "A*B+C"
print(solution(d))