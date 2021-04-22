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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    opStack = ArrayStack()

    prec = {
        '*': 3, '/': 3,
        '+': 2, '-': 2,
        '(': 1,
    }
    
    postfixList = []
    for c in tokenList :
        if c in prec :
            if c == '(' :
                opStack.push(c)
            else :
                if opStack.isEmpty() :
                    opStack.push(c)
                else :
                    while opStack.size() > 0 :
                        if prec[opStack.peek()] >= prec[c] :
                            #answer += '{}'.format(opStack.pop())
                            postfixList.append(opStack.pop())
                        else :
                            break
                    opStack.push(c)
        elif c == ')' :
            while not opStack.isEmpty() :
                t = opStack.pop()
                if t == '(' :
                    break
                else :
                    #answer += '{}'.format(t)
                    postfixList.append(t)
        else :
            #answer += '{}'.format(c)
            postfixList.append(c)
            
    while not opStack.isEmpty() :
        #answer += '{}'.format(opStack.pop())
        postfixList.append(opStack.pop())
    
    return postfixList


def postfixEval(tokenList):
    op = ['+', '-', '*', '/']
    evalStack = ArrayStack()
    
    for token in tokenList :
        if token not in op :
            evalStack.push(token)
        elif token == '+' :
            oper1 = evalStack.pop()
            oper2 = evalStack.pop()
            evalStack.push(oper2 + oper1)
        elif token == '-' :
            oper1 = evalStack.pop()
            oper2 = evalStack.pop()
            evalStack.push(oper2 - oper1)
        elif token == '*' :
            oper1 = evalStack.pop()
            oper2 = evalStack.pop()
            evalStack.push(oper2 * oper1)
        elif token == '/' :
            oper1 = evalStack.pop()
            oper2 = evalStack.pop()
            evalStack.push(oper2 / oper1)
            
    return evalStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

a = "5 + 3"
b = "(1 + 2) * (3 + 4)"
c = "7 * (9 - (3+2))"
print(solution(c))