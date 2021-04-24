def solution(s):
    answer = True

    stack = []

    for c in s :
        if c in '({[' :
            stack.append(c)
        else :
            if len(stack) == 0 :
                answer = False
                break
            elif c == ')' and stack.pop() != '(':
                answer = False
                break
            elif c == '}' and stack.pop() != '{':
                answer = False
                break
            elif c == ']' and stack.pop() != '[':
                answer = False
                break
    else :
        if len(stack) != 0 :
            answer = False   

    return answer

print(solution("{{}}"))
print(solution("({})[]"))
print(solution("[)"))
print(solution("]()["))
print(solution("([())]"))
