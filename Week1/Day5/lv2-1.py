def solution(s):
    answer = True

    stack = []

    for c in s :
        if c == '(' :
            stack.append(c)
        else :
            if len(stack) == 0 :
                answer = False
                break
            elif c == ')' and stack.pop() != '(':
                answer = False
                break
    else :
        if len(stack) != 0 :
            answer = False   

    return answer