from collections import deque

def solution(strs, t):
    answer = -1

    dq = deque([])

    nowStr = ''
    depth = 0

    dq.append((nowStr, depth))
    while dq :
        nowStr, depth= dq.popleft()

        if nowStr == t :
            answer = depth
            break

        for item in strs :
            newStr = ''.join([nowStr, item])
            if newStr == t[:len(newStr)] :
                dq.append((newStr, depth+1))

    return answer

print(solution(["ba","na","n","a"], 'banana'))
print(solution(["app","ap","p","l","e","ple","pp"], 'apple'))
print(solution(["ba","an","nan","ban","n"], 'banana'))